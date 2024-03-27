
#ifndef __ROLL_SIDED_DICE_H__
#define __ROLL_SIDED_DICE_H__

#include "../util/vector_functions.h"
#include "constructs/dice_enums.h"
#include "constructs/vec.h"

void roll_plain_sided_dice(vec* x, vec* y, vec* result, EXPLOSION_TYPE explode,
                           long long start_offset);

void roll_symbolic_dice(vec* x, vec* y, vec* result);

#endif
