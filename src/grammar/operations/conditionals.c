#include "conditionals.h"

#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

#include "rolls/dice_core.h"
#include "shared_header.h"
#include "util/safe_functions.h"
#include "util/vector_functions.h"
#include "util/array_functions.h"

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
int check_condition(vec* x, vec* y, COMPARATOR c) {
  if (gnoll_errno) return 1;

  if(c == IS_UNIQUE || c == IF_ODD || c == IF_EVEN){
      return check_condition_vector(x, c);
  }else{

      long long xvalue = collapse(x->storage.content, x->length);
      long long yvalue = y->storage.content[0];
      return check_condition_scalar(xvalue, yvalue, c);
  }
}

int check_condition_vector(vec* v, COMPARATOR c) {
   switch (c){
     case IS_UNIQUE: {
       gnoll_errno = NOT_IMPLEMENTED;
       return 1;
     }
     case IF_EVEN:{
        long long x = collapse(v->storage.content, v->length);
        return (x+1) % 2;
     }
     case IF_ODD: {
        long long x = collapse(v->storage.content, v->length);
        return x % 2;
     }
     default: {
       gnoll_errno = NOT_IMPLEMENTED;
       return 0;
     }
   }
}

int check_condition_scalar(long lomg x, long long y, COMPARATOR c) {
  if (gnoll_errno) return 1;

  long long xvalue = x;
  long long yvalue = y;
  switch (c) {
    case EQUALS: {
      return xvalue == yvalue;
    }
    case NOT_EQUAL: {
      return xvalue != yvalue;
    }
    case LESS_THAN: {
      return xvalue < yvalue;
    }
    case GREATER_THAN: {
      return xvalue > yvalue;
    }
    case LESS_OR_EQUALS: {
      return xvalue <= yvalue;
    }
    case GREATER_OR_EQUALS: {
      return xvalue >= yvalue;
    }
    case IS_UNIQUE: {
      // Unique by the fact that it is scalar
      return 1;
    }
    case IF_ODD: {
      return x % 2;
    }
    case IF_EVEN: {
      return (x+1) % 2;
    }
    case INVALID: {
      printf("Invalid Conditional\n");
      gnoll_errno = UNDEFINED_BEHAVIOUR;
      return 0;
    }
    default: {
      printf("Unknown Conditional\n");
      gnoll_errno = UNDEFINED_BEHAVIOUR;
      return 0;
    }
  }
  printf("Unknown Conditional\n");
  gnoll_errno = UNDEFINED_BEHAVIOUR;
  return 1;
}
