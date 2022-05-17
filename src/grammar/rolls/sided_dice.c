#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include "dice_logic.h"
#include "vector_functions.h"
#include <stdlib.h>
#include <stdio.h>


int roll_plain_sided_dice(vec * x, vec * y, vec * result){
    // XdY
    int num_dice = x->content[0];
    int sides = y->content[0];

    int err = validate_roll(num_dice, sides);
    if (err){
        return 1;
    }else{
        // e.g. d4, it is implied that it is a single dice
        roll_params rp;
        rp.number_of_dice = num_dice;
        rp.die_sides = sides;
        rp.explode = false;
        int * roll_result = do_roll(rp);

        initialize_vector(result, NUMERIC, num_dice);
        result->content = roll_result;
        result->source = rp;
    }
    return 0;
}