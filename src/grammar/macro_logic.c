
#include "uthash.h"
#include "vector_functions.h"
#include "macro_logic.h"
#include "shared_header.h"
#include "safe_functions.h"
#include "yacc_header.h"

struct macro_struct *macros = NULL; //Initialized to NULL (Importnat)
extern int gnoll_errno;

void register_macro(vec * macro_name, roll_params *to_store) {
    if(gnoll_errno){return;}

    char * skey = macro_name->symbols[0];   
    int key = safe_strtol(skey, NULL, 10);
    if(gnoll_errno){return;}

    struct macro_struct *s;

    HASH_FIND_INT(macros, &key, s);  /* id already in the hash? */
    if (s == NULL){
        s = (struct macro_struct*)safe_malloc(sizeof *s);
        s->stored_dice_roll.symbol_pool = (char **)safe_malloc(to_store->die_sides);
        for(unsigned int i = 0; i != to_store->die_sides; i++){
            s->stored_dice_roll.symbol_pool[i] = (char *)safe_malloc(MAX_SYMBOL_LENGTH);
        }
        if(gnoll_errno){return;}
        s->id = key;
        HASH_ADD_INT(macros, id, s);  /* id: name of key field */
    }

    memcpy(&s->stored_dice_roll, to_store, sizeof(*to_store));
    
    for(unsigned int i = 0; i != to_store->die_sides; i++){
        memcpy(&s->stored_dice_roll.symbol_pool[i], &to_store->symbol_pool[i], MAX_SYMBOL_LENGTH);
    }
}

void search_macros(char * skey, roll_params *to_store) {
    if(gnoll_errno){return ;}
    (void)(to_store); // will be refactored later

    int key = safe_strtol(skey, NULL, 10);
    if(gnoll_errno){return ;}

    struct macro_struct *s;

    HASH_FIND_INT(macros, &key, s);  /* s: output pointer */

    // to_store = &s->stored_dice_roll;
    // memcpy(to_store, &s->stored_dice_roll, sizeof(roll_params));
    *to_store = s->stored_dice_roll;
    to_store->symbol_pool = s->stored_dice_roll.symbol_pool;

    memcpy(
        to_store->symbol_pool, 
        s->stored_dice_roll.symbol_pool, 
        s->stored_dice_roll.number_of_dice*sizeof(int*)
    );
    
    for(unsigned int i = 0; i != to_store->die_sides; i++){
        memcpy(to_store->symbol_pool[i], s->stored_dice_roll.symbol_pool[i], MAX_SYMBOL_LENGTH);
    }
}
