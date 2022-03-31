#ifndef SHARED_YACC_HEADER
#define SHARED_YACC_HEADER

#include <stdbool.h>

typedef enum {
    // 0 is invalid
    SYMBOLIC=1,
    NUMERIC=2
} DIE_TYPE;

typedef enum {
    NO_MOCK=0,
    RETURN_CONSTANT=1,
    RETURN_INCREMENTING=2,
    RETURN_DECREMENTING=3
} MOCK_METHOD;

typedef struct vec{
    DIE_TYPE dtype;
    int * content;
    unsigned int length;
    char ** symbols;
} vec;

int roll(char * s);
int roll_and_write(char * s, char * f);
int mock_roll(char * s, char * f, int mock_value, bool quiet, int mock_const);

#endif