#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include <stdlib.h>
#include <stdio.h>

int random_fn_run_count = 0;


void reset_mocking(){
    random_fn_run_count = 0;
}

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

unsigned int perform_roll(
    int number_of_dice,
    int die_sides,
    bool explode,
    MOCK_METHOD mock_style,
    int mock_constant
)
{
    int explosion_result = 0;
    int explosion_condition_score = 0;

    int all_dice_roll = 0;
    int single_die_roll = 0;
    int final_result = 0;
    do{
        all_dice_roll = 0;
        for(int i = 0; i < number_of_dice; i++){
            // TODO: Don't hardocde 1
            single_die_roll = random_fn(1, die_sides,mock_style, mock_constant);
            all_dice_roll += single_die_roll;
        }
        explosion_condition_score = number_of_dice*die_sides;
        explosion_result += all_dice_roll;
    }while(explode && (all_dice_roll == explosion_condition_score));

    final_result = explosion_result;
    return final_result;
}


unsigned int do_roll(roll_params rp){
    return perform_roll(
        rp.number_of_dice,
        rp.die_sides,
        rp.explode,
        rp.mock_style,
        rp.mock_constant
    );
}

int validate_roll(int number_of_dice, int die_side)
{
    if (die_side < 0){
        printf("Cannot roll a dice with a negative amount of sides\n");
        return 1;
    }
    return 0;
}
