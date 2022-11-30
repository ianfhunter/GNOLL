#ifndef __VEC_H__
#define __VEC_H__

#include "constructs/dice_enums.h"
#include "constructs/roll_parameters.h"
#include <stdbool.h>

typedef struct vec {
  DIE_TYPE dtype;
  int* content;
  unsigned int length;
  // TODO: Split length into content_length and symbol length
  //  maybe use union? If it exists in c
  char** symbols;
  roll_params source;
  bool has_source;
} vec;

#endif
