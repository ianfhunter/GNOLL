
#include "operations/macro_logic.h"

#include "external/uthash.h"
#include "shared_header.h"
#include "util/safe_functions.h"
#include "util/vector_functions.h"
#include "yacc_header.h"

// Initialized to NULL (Important)
struct macro_struct *macros = NULL;

extern int gnoll_errno;

unsigned long hash_function(unsigned char *str) {
  /**
   * @brief DJB2 hashing algorithm from http://www.cse.yorku.ca/~oz/hash.html
   *
   * @param str string to encode
   * @return numeric hash encoding
   */

  unsigned long hash = 5381;
  int c;

  while ((c = *str++)) {
    hash = ((hash << 5) + hash) + (unsigned int)c; /* hash * 33 + c */
  }
  return hash;
}

void register_macro(vec *macro_name, roll_params *to_store) {
  /**
   * @brief Register a Macro in GNOLL
   *
   * @param macro_name - Unique name for macro reference
   * @param to_store - Structure containing information on how to roll the dice
   * referenced to by the key
   */

  if (gnoll_errno) {
    return;
  }

  char *skey = macro_name->symbols[0];
  unsigned long key = hash_function((unsigned char *)skey);
  int k = (int)key;
  if (gnoll_errno) {
    return;
  }

  struct macro_struct *s;

  unsigned short int is_symbolic = to_store->dtype == SYMBOLIC;
  HASH_FIND_INT(macros, &k, s); // id already in the hash? 
  
  
  if (s == NULL) {
    s = (struct macro_struct *)safe_malloc(sizeof *s);

    if (gnoll_errno) {
      return;
    }
    s->id = (int)key;
    HASH_ADD_INT(macros, id, s); // id: name of key field 
  }
  
  
  memcpy(&s->stored_dice_roll, to_store, sizeof(*to_store));
  s->stored_dice_roll.symbol_pool = NULL;
  
  if (is_symbolic) {
    free_2d_array(&s->stored_dice_roll.symbol_pool,
                  s->stored_dice_roll.die_sides);
    safe_copy_2d_chararray_with_allocation(
        &s->stored_dice_roll.symbol_pool, to_store->symbol_pool,
        to_store->die_sides, MAX_SYMBOL_LENGTH);
  }
  
  //free(s); //new
  //free(skey); //new
}

void search_macros(char *skey, roll_params *to_store) {
  /**
   * @brief Search for a registered macro
   *
   * @param macro_name - Unique name for macro reference
   * @param to_store - Where to store the macro, if found
   */
  if (gnoll_errno) {
    return;
  }
  
  unsigned long key = hash_function((unsigned char *)skey);
  int k = (int)key;

  if (gnoll_errno) {
    return;
  }

  struct macro_struct *s;

  HASH_FIND_INT(macros, &k, s); /* s: output pointer */

  if (s == NULL) {
    gnoll_errno = UNDEFINED_MACRO;
    return;
  }

  *to_store = s->stored_dice_roll;
  to_store->symbol_pool = NULL;

  unsigned short int is_symbolic = to_store->dtype == SYMBOLIC;

  if (is_symbolic) {
    free_2d_array(&to_store->symbol_pool, to_store->die_sides);
    safe_copy_2d_chararray_with_allocation(
        &to_store->symbol_pool, s->stored_dice_roll.symbol_pool,
        to_store->die_sides, MAX_SYMBOL_LENGTH);
  }
}
