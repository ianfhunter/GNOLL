#ifndef __VEC_H__
#define __VEC_H__

#include "constructs/dice_enums.h"
#include "constructs/roll_parameters.h"
#include <stdbool.h>

typedef struct vec {
  DIE_TYPE dtype;
  union {
    long long* content;
    char** symbols;
  }
  unsigned long long length;
  // TODO: Split length into content_length and symbol length
  roll_params source;
  bool has_source;
} vec;

#endif
