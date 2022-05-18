#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include "dice_logic.h"
#include "vector_functions.h"
#include "condition_checking.h"
#include <stdlib.h>
#include <stdio.h>

bool check_condition(
    vec * x, 
    vec * y, 
    COMPARATOR c
){
    // TODO: How will reroll work with >1 Value?
    // - Collapse
    // - Element-Wise Checking? (1-N, N-N, N-1 considations)
    switch(c){
        case EQUALS:{
            return x->content[0] == y->content[0];
        }
        case NOT_EQUAL:{
            return x->content[0] != y->content[0];
        }
        case LESS_THAN:{
            return x->content[0] < y->content[0];
        }
        case GREATER_THAN:{
            return x->content[0] > y->content[0];
        }
        case LESS_OR_EQUALS:{
            return x->content[0] <= y->content[0];
        }
        case GREATER_OR_EQUALS:{
            return x->content[0] >= y->content[0];
        }
    }
}