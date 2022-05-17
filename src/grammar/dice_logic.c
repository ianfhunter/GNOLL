#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include <stdlib.h>
#include <stdio.h>


#define EXPLOSION_LIMIT 50

int random_fn_run_count = 0;
int global_mock_value = 0;
int secondary_mock_value = 0;
MOCK_METHOD global_mock_style = NO_MOCK;


void reset_mocking(){
    random_fn_run_count = 0;
    global_mock_value = 0;
    global_mock_style=NO_MOCK;
}
void init_mocking(MOCK_METHOD mock_style, int starting_value){
    global_mock_value = starting_value;
    global_mock_style=mock_style;
}

void mocking_tick(){
    switch(global_mock_style){
        case RETURN_INCREMENTING: {
            global_mock_value = global_mock_value+1;
            break;    
        }
        case RETURN_DECREMENTING: {
            global_mock_value = global_mock_value-1;
            break;    
        }
        case RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE: {
            if (random_fn_run_count == 1){
                secondary_mock_value = global_mock_value;
            }
            if(random_fn_run_count < 2){
                global_mock_value = secondary_mock_value;
            }else{
                global_mock_value = 1;
            }
            break;    
        }
        default:
            break;
    }
}


int random_fn(int small, int big){
    random_fn_run_count++;

    if(small == big){
        return big;
    }
    if(small > big ){
        // e.g. roll a minus sided die.
        // d0 -> {1...0}
        return big;
    };

    int value = 0;
    if (global_mock_style == NO_MOCK){
        value = rand()%(big+1-small)+small;
    }else{
        value = global_mock_value;
        mocking_tick();
    }
    // printf("Dice Roll Value: %i\n", value);
    return value;
}

unsigned int * perform_roll(
    int number_of_dice,
    int die_sides,
    bool explode
)
{
    int explosion_condition_score = 0;
    int explosion_count = 0;

    int * all_dice_roll = calloc(number_of_dice, sizeof(int));
    int single_die_roll = 0;
    int exploded_result = 0;

    for(int i = 0; i < number_of_dice; i++){
        all_dice_roll[i] = 0;
    }

    do{
        for(int i = 0; i < number_of_dice; i++){

            // TODO: Don't hardcode 1
            single_die_roll = random_fn(1, die_sides);
            all_dice_roll[i] += single_die_roll;   

            exploded_result += single_die_roll;
        }
        explosion_condition_score += number_of_dice*die_sides;
        
        explosion_count++;
    }while(explode && (exploded_result == explosion_condition_score) && explosion_count < EXPLOSION_LIMIT);

    return all_dice_roll;
}


unsigned int * do_roll(roll_params rp){
    // printf("Number of Dice: %i\n", rp.number_of_dice);
    // printf("Die Sides: %i\n", rp.die_sides);
    // printf("Explode: %i\n", rp.explode);
    return perform_roll(
        rp.number_of_dice,
        rp.die_sides,
        rp.explode
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
