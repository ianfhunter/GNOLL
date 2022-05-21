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
bool check_condition(
    vec * x, 
    vec * y, 
    COMPARATOR c
){
    int dvalue = collapse(x->content, x->length);
    int cvalue = y->content[0];
    switch(c){
        case EQUALS:{
            return dvalue == cvalue;
        }
        case NOT_EQUAL:{
            return dvalue != cvalue;
        }
        case LESS_THAN:{
            return dvalue < cvalue;
        }
        case GREATER_THAN:{
            return dvalue > cvalue;
        }
        case LESS_OR_EQUALS:{
            return dvalue <= cvalue;
        }
        case GREATER_OR_EQUALS:{
            return dvalue >= cvalue;
        }
    }
}