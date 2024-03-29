#ifndef __DIE_LOGIC_H__
#define __DIE_LOGIC_H__

#include "constructs/dice_enums.h"
#include "shared_header.h"

// #ifdef __cplusplus
// extern "C" {
// #endif


// Random Functions
long long random_fn(long long small, long long big);

// Rolling Functions
long long* perform_roll(
    unsigned long long number_of_dice, 
    unsigned long long die_sides,
    EXPLOSION_TYPE explode, 
    long long start_value
);
long long* do_roll(roll_params rp);

// #ifdef __cplusplus
// }
// #endif

#endif
