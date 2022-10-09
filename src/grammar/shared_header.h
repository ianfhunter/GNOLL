#ifndef SHARED_YACC_HEADER
#define SHARED_YACC_HEADER

#include "vector_functions.h"
#include "rolls/sided_dice.h"

typedef enum {
    NO_MOCK=0,
    RETURN_CONSTANT=1,
    RETURN_INCREMENTING=2,
    RETURN_DECREMENTING=3,
    RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE=4
} MOCK_METHOD;

typedef enum {
    SUCCESS=0,
    BAD_ALLOC=1,
    BAD_FILE=2,
    NOT_IMPLEMENTED=3,
    INTERNAL_ASSERT=4,
    UNDEFINED_BEHAVIOUR=5,
    BAD_STRING=6
} ERROR_CODES;

int roll(char * s);
int roll_and_write(char * s, char * f);
int mock_roll(char * s, char * f, int mock_value, int quiet, int mock_const);

#endif
