#ifndef __DICE_ROLL_STRUCTS_H__
#define __DICE_ROLL_STRUCTS_H__

#include "dice_enums.h"

typedef struct roll_params{
    int number_of_dice;
    int die_sides;
    EXPLOSION_TYPE explode;
    char ** symbol_pool;
} roll_params;

#endif