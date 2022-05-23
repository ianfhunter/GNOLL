
#ifndef __MACRO_LOGIC_H
#define __MACRO_LOGIC_H

#include "uthash.h"
#include "vector_functions.h"


// TODO: It would be better to fit arbitrary length strings.

struct macro_struct {
    int id;                    /* key */
    // char name[MAX_SYMBOL_TEXT_LENGTH];
    vec stored_dice_roll;
    UT_hash_handle hh;         /* makes this structure hashable */
};

void register_macro(char * skey, vec *to_store);

struct macro_struct *search_macros(char * skey, vec *to_store);

#endif