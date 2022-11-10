#ifndef SHARED_YACC_HEADER
#define SHARED_YACC_HEADER

#include "rolls/sided_dice.h"
#include "util/vector_functions.h"

// #ifdef __cplusplus
// extern "C" {
// #endif

typedef enum {
  NO_MOCK = 0,
  RETURN_CONSTANT = 1,
  RETURN_INCREMENTING = 2,
  RETURN_DECREMENTING = 3,
  RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE = 4
} MOCK_METHOD;

int roll(char* s);
int roll_with_breakdown(char * s);
int roll_and_write(char* s, char* f);
void roll_and_write_R(int* return_code, char** s, char** f );
int mock_roll(char* s, char* f, int mock_value, int mock_const);

// #ifdef __cplusplus
// }
// #endif

#endif
