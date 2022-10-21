#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include "dice_logic.h"
#include "vector_functions.h"
#include "safe_functions.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

extern int gnoll_errno;

void roll_plain_sided_dice(
    vec * x,
    vec * y,
    vec * result,
    EXPLOSION_TYPE explode,
    int start_offset
){
    if(gnoll_errno) return;

    // XdY
    unsigned int num_dice = (unsigned int)x->content[0];
    unsigned int sides = (unsigned int)y->content[0];

    // e.g. d4, it is implied that it is a single dice
    roll_params rp;
    rp.dtype = NUMERIC;
    rp.number_of_dice = num_dice;
    rp.die_sides = sides;
    rp.explode = explode;
    rp.start_value = start_offset;
    int * roll_result = do_roll(rp);
    initialize_vector(result, NUMERIC, num_dice);
    result->content = roll_result;
    result->source = rp;
}

void roll_symbolic_dice(vec * x, vec * y, vec * result){
    if(gnoll_errno) return;

    // XdY
    unsigned int num_dice = (unsigned int)x->content[0];

    // e.g. d4, it is implied that it is a single dice
    roll_params rp;
    rp.dtype = SYMBOLIC;
    rp.number_of_dice = num_dice ;
    rp.die_sides = y->length;
    rp.explode = 0;
    rp.symbol_pool = NULL;

    // Copy over memory to Symbol Pool for reloading
    
    free_2d_array(&rp.symbol_pool, rp.die_sides);
    safe_copy_2d_chararray_with_allocation(
        &rp.symbol_pool,
        y->symbols,
        y->length,
        MAX_SYMBOL_LENGTH
    );
    rp.start_value = 0; // First index of array

    int * indexes = do_roll(rp);

    extract_symbols(y->symbols, result->symbols, indexes, rp.number_of_dice);
}
