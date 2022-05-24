#ifndef __DIE_LOGIC_H__
#define __DIE_LOGIC_H__

#include "shared_header.h"
#include "rolls/dice_enums.h"

// Mocking Util
void reset_mocking();
void init_mocking(MOCK_METHOD mock_style, int starting_value);

// Random Functions
int random_fn(int small, int big );

// Rolling Functions
unsigned int * perform_roll(
    int number_of_dice,
    int die_sides,
    EXPLOSION_TYPE explode
);
unsigned int * do_roll(
    roll_params rp
);

// Verification
int validate_roll(int number_of_dice, int die_side);

#endif