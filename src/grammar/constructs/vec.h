#ifndef __VEC_H__
#define __VEC_H__

#include "constructs/dice_enums.h"
#include "constructs/roll_parameters.h"
#include <stdbool.h>

typedef struct vec {
  DIE_TYPE dtype;

  union { // Vectors can only contain one dice type
    long long* content;
    char** symbols;
  } storage;
  unsigned long long length;

  roll_params source;
  bool has_source;
} vec;

#endif
