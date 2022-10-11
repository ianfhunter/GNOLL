#ifndef __VEC_H__
#define __VEC_H__

#include "dice_enums.h"
#include "dice_roll_structs.h"

typedef struct vec{
    DIE_TYPE dtype;
    int * content;
    unsigned int length;
    //TODO: Split length into content_length and symbol length
    // maybe use union? If it exists in c
    char ** symbols;
    roll_params source;
} vec;

#endif
