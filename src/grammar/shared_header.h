#ifndef SHARED_YACC_HEADER
#define SHARED_YACC_HEADER

typedef enum {SYMBOLIC, NUMERIC} DIE_TYPE;

typedef struct vec{
    DIE_TYPE dtype;
    int * content;
    unsigned int length;
    char ** symbols;
} vec;

#endif