#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include "dice_logic.h"
#include "vector_functions.h"
#include <stdlib.h>
#include <stdio.h>

extern int gnoll_errno;

int roll_plain_sided_dice(
    vec * x,
    vec * y,
    vec * result,
    EXPLOSION_TYPE explode,
    int start_offset
){
    if(gnoll_errno) return 0;


    // XdY
    unsigned int num_dice = x->content[0];
    unsigned int sides = y->content[0];

    int err = validate_roll(num_dice, sides);
    if (err){
        printf("Validation Error\n");
        return 1;
    }else{
        // e.g. d4, it is implied that it is a single dice
        roll_params rp;
        rp.number_of_dice = num_dice;
        rp.die_sides = sides;
        rp.explode = explode;
        rp.start_value = start_offset;
        int * roll_result = do_roll(rp);
        initialize_vector(result, NUMERIC, num_dice);
        result->content = roll_result;
        result->source = rp;
    }
    return 0;
}

int roll_symbolic_dice(vec * x, vec * y, vec * result){
    if(gnoll_errno) return 0;

    // XdY
    unsigned int num_dice = x->content[0];

    int err = validate_roll(num_dice, 1);
    if (err){
        return 1;
    }else{
        // e.g. d4, it is implied that it is a single dice
        roll_params rp;
        rp.number_of_dice = num_dice ;
        rp.die_sides = y->length;
        rp.explode = 0;
        rp.symbol_pool = y->symbols;
        rp.start_value = 0; // First index of array

        int * indexes = do_roll(rp);

        extract_symbols(y->symbols, result->symbols, indexes, rp.number_of_dice);

    }
    return 0;
}