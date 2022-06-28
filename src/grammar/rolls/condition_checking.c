#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include "dice_logic.h"
#include "vector_functions.h"
#include "condition_checking.h"
#include <stdlib.h>
#include <stdio.h>

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
    int xvalue = collapse(x->content, x->length);
    int yvalue = y->content[0];
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
    }
}

int check_condition_scalar(
    int x, 
    int y, 
    COMPARATOR c
){
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
    }
}