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
    RETURN_DECREMENTING=3,
    RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE=4
} MOCK_METHOD;

typedef struct roll_params{
    int number_of_dice;
    int die_sides;
    bool explode;
} roll_params;

typedef struct vec{
    DIE_TYPE dtype;
    int * content;
    unsigned int length;
    //TODO: Split length into content_length and symbol length
    // maybe use union? If it exists in c
    char ** symbols;
    roll_params source;
} vec;

int roll(char * s);
int roll_and_write(char * s, char * f);
int mock_roll(char * s, char * f, int mock_value, bool quiet, int mock_const);

#endif