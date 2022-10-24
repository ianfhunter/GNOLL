
#ifndef __ROLL_SIDED_DICE_H__
#define __ROLL_SIDED_DICE_H__

#include "../util/vector_functions.h"
#include "dice_enums.h"
#include "vec.h"

void roll_plain_sided_dice(
    vec * x, 
    vec * y, 
    vec * result,
    EXPLOSION_TYPE explode,
    int start_offset
);

void roll_symbolic_dice(
    vec * x, 
    vec * y, 
    vec * result
);

#endif
