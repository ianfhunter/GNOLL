#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include "rolls/dice_logic.h"
#include "util/vector_functions.h"
#include "util/safe_functions.h"
#include "condition_checking.h"
#include <stdlib.h>
#include <stdio.h>

extern int gnoll_errno;

/**
 * @brief Comparision of a collapsed vector to a value
 * 
 * @param x vector containing dice rolls
 * @param y vector containing 1 comparision value
 * @param c enum indicating comparsion type
 * @return true - the condition is True
 * @return false - the condition is False
 */
int check_condition(
    vec * x, 
    vec * y, 
    COMPARATOR c
){
    if(gnoll_errno) return 1;

    int xvalue = collapse(x->content, x->length);
    int yvalue = y->content[0];

    return check_condition_scalar(xvalue, yvalue, c);
}

int check_condition_scalar(
    int x, 
    int y, 
    COMPARATOR c
){
    if(gnoll_errno) return 1;

    int xvalue = x;
    int yvalue = y;
    switch(c){
        case EQUALS:{
            return xvalue == yvalue;
        }
        case NOT_EQUAL:{
            return xvalue != yvalue;
        }
        case LESS_THAN:{
            return xvalue < yvalue;
        }
        case GREATER_THAN:{
            return xvalue > yvalue;
        }
        case LESS_OR_EQUALS:{
            return xvalue <= yvalue;
        }
        case GREATER_OR_EQUALS:{
            return xvalue >= yvalue;
        }
        case UNIQUE:{
            // Unique by the fact that it is scalar
            return 1;
        }
        case INVALID:{
            printf("Invalid Conditional\n");
            gnoll_errno = UNDEFINED_BEHAVIOUR;
            return 1;
        }
        default:{
            printf("Unknown Conditional\n");
            gnoll_errno = UNDEFINED_BEHAVIOUR;
            return 1;
        }
    }
    printf("Unknown Conditional\n");
    gnoll_errno = UNDEFINED_BEHAVIOUR;
    return 1;
}
