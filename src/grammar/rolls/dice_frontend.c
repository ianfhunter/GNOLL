#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "rolls/dice_core.h"
#include "shared_header.h"
#include "util/safe_functions.h"
#include "util/vector_functions.h"
#include "shared_header.h"

extern int gnoll_errno;

void roll_plain_sided_dice(vec* x, vec* y, vec* result, EXPLOSION_TYPE explode,
                           long long start_offset) {
  /**
   * @brief Roll numeric dice
   * @param x - Amount of dice (xDy)
   * @param y - Dice Sides (xDy)
   * @param result - Where to store the dice roll result
   * @param explode Explosion logic to apply (if applicable)
   * @param start_offset offset each dice roll by this amount
   */
  if (gnoll_errno) return;

  // XdY
  unsigned long long num_dice = (unsigned long long)x->content[0];
  unsigned long long sides = (unsigned long long)y->content[0];

  // e.g. d4, it is implied that it is a single dice
  roll_params rp;
  rp.dtype = NUMERIC;
  rp.number_of_dice = num_dice;
  rp.die_sides = sides;
  rp.explode = explode;
  rp.start_value = start_offset;
  long long* roll_result = do_roll(rp);

#if USE_CLT
  // Must Accumulate. Loses details of per-item values
  initialize_vector(result, NUMERIC, 1);
#else
  initialize_vector(result, NUMERIC, num_dice);
#endif
  free(result->content);
  result->content = roll_result;
  result->source = rp;
  result->has_source = true;
}

void roll_symbolic_dice(vec* x, vec* y, vec* result) {
  /**
   * @brief Roll symbolic dice
   * @param x - Amount of dice (xDy)
   * @param y - Dice Sides (xDy)
   * @param result - Where to store the dice roll result
   */
  if (gnoll_errno) return;

#if USE_CLT
    printf("Cannot use Central Limit Therom Optimization with Symbolic Dice\n");
    gnoll_errno = NOT_IMPLEMENTED;
    return;
#endif

  unsigned long long num_dice = (unsigned long long)x->content[0];

  // e.g. d4, it is implied that it is a single dice
  roll_params rp;
  rp.dtype = SYMBOLIC;
  rp.number_of_dice = num_dice;
  rp.die_sides = y->length;
  rp.explode = (EXPLOSION_TYPE)0;
  rp.symbol_pool = NULL;

  // Copy over memory to Symbol Pool for reloading
  safe_copy_2d_chararray_with_allocation(
    &rp.symbol_pool, 
    y->symbols, 
    y->length,
    MAX_SYMBOL_LENGTH
  );

  rp.start_value = 0;  // First index of array

  long long* indexes = do_roll(rp);

  free_2d_array(&rp.symbol_pool, y->length);

  extract_symbols(y->symbols, result->symbols, indexes, rp.number_of_dice);
  free(indexes);
}
