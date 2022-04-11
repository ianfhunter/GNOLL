#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include <stdlib.h>
#include <stdio.h>

int random_fn_run_count = 0;

int random_fn(int small, int big, MOCK_METHOD mock_style, int mock_constant ){

    if(small >= big ){
        return big;
    };

    if (mock_style == NO_MOCK){
        return rand()%(big+1-small)+small;
    }
    if (mock_style == RETURN_CONSTANT){
        return mock_constant;
    }
    if (mock_style == RETURN_INCREMENTING){
        // Handled Externally
        return mock_constant;
    }
    if (mock_style == RETURN_DECREMENTING){
        // Handled Externally
        return mock_constant;
    }
    if (mock_style == RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE){
        random_fn_run_count++;
        if(random_fn_run_count >= 3){
            return 1;
        }else{
            return mock_constant;
        }
    }
}

unsigned int perform_roll(int number_of_dice, int die_sides)
{
    return roll_numeric_die(number_of_dice, die_sides);
}
int validate_roll(int number_of_dice, int die_side)
{
    if (die_side < 0){
        printf("Cannot roll a dice with a negative amount of sides\n");
        return 1;
    }
    return 0;
}
