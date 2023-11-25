
#ifndef __MACRO_LOGIC_H
#define __MACRO_LOGIC_H

#include "external/uthash.h"
#include "constructs/roll_parameters.h"
#include "util/vector_functions.h"

unsigned long hash_function(unsigned char *str);

struct macro_struct {
  int id; /* key */
  roll_params stored_dice_roll;
  UT_hash_handle hh; /* makes this structure hashable */
};

void delete_all_macros(void);

void register_macro(vec *macro_name, roll_params *to_store);

void search_macros(char *skey, roll_params *to_store);

#endif
