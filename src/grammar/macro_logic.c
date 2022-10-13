
#include "uthash.h"
#include "vector_functions.h"
#include "macro_logic.h"
#include "shared_header.h"
#include "safe_functions.h"

struct macro_struct *macros = NULL; //Initialized to NULL (Importnat)
extern int gnoll_errno;


void register_macro(vec * macro_name, vec *to_store) {
    if(gnoll_errno) return;

    char * skey = macro_name->symbols[0];
    int key = safe_strtol(skey, NULL, 10);
    if(gnoll_errno) return;

    struct macro_struct *s;

    HASH_FIND_INT(macros, &key, s);  /* id already in the hash? */
    if (s == NULL){
        s = (struct macro_struct*)safe_malloc(sizeof *s);
        if(gnoll_errno){return};
        s->id = key;
        HASH_ADD_INT(macros, id, s);  /* id: name of key field */
    }
    memcpy(&s->stored_dice_roll, to_store, sizeof(*to_store));
}

struct macro_struct *search_macros(char * skey, vec *to_store) {
    if(gnoll_errno) return NULL;
    (void)(to_store); // will be refactored later

    int key = safe_strtol(skey, NULL, 10);
    if(gnoll_errno) return NULL;

    struct macro_struct *s;

    HASH_FIND_INT(macros, &key, s);  /* s: output pointer */
    return s;
}
