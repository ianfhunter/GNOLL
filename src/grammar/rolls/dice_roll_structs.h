#ifndef __DICE_ROLL_STRUCTS_H__
#define __DICE_ROLL_STRUCTS_H__

#include "dice_enums.h"

typedef struct roll_params{
    unsigned int number_of_dice;
    unsigned int die_sides;
    EXPLOSION_TYPE explode;
    char ** symbol_pool;
    int start_value;
} roll_params;

#endif