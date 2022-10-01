#include <stddef.h>
#include "shared_header.h"
#include "yacc_header.h"
#include "dice_logic.h"
#include "vector_functions.h"
#include "condition_checking.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * @brief 
 * @param x vector containing dice rolls
 * @return maximum dice in vector
 */
int max(
    vec * x, 
){ 
    int max = 0; // TODO: Min Int
    for (int i=0;i!=x->length:i++){
        int v = x->content[i];
        if (v > max){
           max = v;
        }
    }
    //Todo: return vector 
    return max;
}
