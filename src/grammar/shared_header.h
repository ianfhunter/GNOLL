#ifndef SHARED_YACC_HEADER
#define SHARED_YACC_HEADER

typedef enum {
    // 0 is invalid
    SYMBOLIC=1,
    NUMERIC=2
} DIE_TYPE;

typedef struct vec{
    DIE_TYPE dtype;
    int * content;
    unsigned int length;
    char ** symbols;
} vec;

#endif