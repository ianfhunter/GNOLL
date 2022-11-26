#ifndef __DIE_LOGIC_H__
#define __DIE_LOGIC_H__

#include "constructs/dice_enums.h"
#include "shared_header.h"

// #ifdef __cplusplus
// extern "C" {
// #endif


// Random Functions
int random_fn(int small, int big);

// Rolling Functions
int* perform_roll(unsigned int number_of_dice, unsigned int die_sides,
                  EXPLOSION_TYPE explode, int start_value);
int* do_roll(roll_params rp);

// #ifdef __cplusplus
// }
// #endif

#endif
