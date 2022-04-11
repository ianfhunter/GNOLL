#ifndef __DIE_LOGIC_H__
#define __DIE_LOGIC_H__

#include "shared_header.h"

int random_fn(int small, int big, MOCK_METHOD mock_style, int mock_constant );

unsigned int perform_roll(
    int number_of_dice,
    int die_sides,
    bool explode,
    MOCK_METHOD mock_style,
    int mock_constant
);

int validate_roll(int number_of_dice, int die_side);

void reset_mocking();

#endif