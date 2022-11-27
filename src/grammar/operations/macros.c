
#include "operations/macros.h"

#include "external/uthash.h"
#include "shared_header.h"
#include "util/safe_functions.h"
#include "util/vector_functions.h"
#include "shared_header.h"

extern int verbose;

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

void delete_all_macros() {
  struct macro_struct *current_macro, *tmp;

  HASH_ITER(hh, macros, current_macro, tmp) {
    HASH_DEL(macros, current_macro);  /* delete; users advances to next */
    
    free_2d_array(
      &current_macro->stored_dice_roll.symbol_pool,
      current_macro->stored_dice_roll.die_sides
    );
    free(current_macro);             /* optional- if you want to free  */
  }
}

void register_macro(vec *macro_name, roll_params *to_store) {
  /**
   * @brief Register a Macro in GNOLL
   *
   * @param macro_name - Unique name for macro reference
   * @param to_store - Structure containing information on how to roll the dice
   * referenced to by the key
   */

  if (gnoll_errno) {return;}

  struct macro_struct *s;
  char *skey = macro_name->symbols[0];

  if (verbose) printf("Macro:: Get ID\n");
  unsigned long key = hash_function((unsigned char *)skey);
  int k = (int)key;

  unsigned short int is_symbolic = to_store->dtype == SYMBOLIC;
  
  if (verbose) printf("Macro:: Check existance\n");
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
  // s->stored_dice_roll.symbol_pool = NULL;
  
  if (is_symbolic) {
    // free symbols from roll in S 
    // free_2d_array(&s->stored_dice_roll.symbol_pool,
    //               s->stored_dice_roll.die_sides);
    safe_copy_2d_chararray_with_allocation(
        &s->stored_dice_roll.symbol_pool, to_store->symbol_pool,
       to_store->die_sides, MAX_SYMBOL_LENGTH);

    // free_roll_params(to_store);  //new
    // free_2d_array(&to_store->symbol_pool, to_store->die_sides);
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
    if (verbose) printf("Macro:: UNDEFINED (macros.c)\n");
    gnoll_errno = UNDEFINED_MACRO;
    return;
  }

  *to_store = s->stored_dice_roll;
  to_store->symbol_pool = NULL;
  // free_2d_array(&to_store->symbol_pool, to_store->die_sides);

  unsigned short int is_symbolic = to_store->dtype == SYMBOLIC;

  if (is_symbolic) {
    free_2d_array(&to_store->symbol_pool, to_store->die_sides);
    safe_copy_2d_chararray_with_allocation(
      &to_store->symbol_pool, 
      s->stored_dice_roll.symbol_pool,
      to_store->die_sides, 
      MAX_SYMBOL_LENGTH
    );

  }
  /* DO NOT UNCOMMENT. 
     We need to keep 's'
     Otherwise macros are lost after usage
     free(s);
  */

}
