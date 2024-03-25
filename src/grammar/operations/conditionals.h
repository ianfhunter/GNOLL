
#ifndef __ROLL_CONDITION_CHECKING_H__
#define __ROLL_CONDITION_CHECKING_H__

#include "constructs/vec.h"

typedef enum {
  INVALID = 0,
  EQUALS = 1,
  GREATER_THAN = 2,
  LESS_THAN = 3,
  GREATER_OR_EQUALS = 4,
  LESS_OR_EQUALS = 5,
  NOT_EQUAL = 6,
  IS_UNIQUE = 7,
  IF_EVEN = 8,
  IF_ODD = 9,
} COMPARATOR;

bool check_condition(vec* x, vec* y, COMPARATOR c);

bool check_condition_scalar(long long x, long long y, COMPARATOR c);
bool check_condition_vector(vec* v, COMPARATOR c);
#endif
