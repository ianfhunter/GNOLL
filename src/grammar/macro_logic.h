
#ifndef __MACRO_LOGIC_H
#define __MACRO_LOGIC_H

#include "uthash.h"
#include "vector_functions.h"
#include "rolls/dice_rolls_structs.h"

struct macro_struct {
    int id;                    /* key */
    // char name[MAX_SYMBOL_LENGTH];
    roll_params stored_dice_roll;
    UT_hash_handle hh;         /* makes this structure hashable */
};

void register_macro(vec *macro_name, roll_params *to_store);

struct macro_struct *search_macros(char * skey, roll_params *to_store);

#endif
