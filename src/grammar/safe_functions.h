#ifndef __SAFE_FNS_H__
#define __SAFE_FNS_H__

#include <stdio.h>
#include <stdlib.h>
#include "shared_header.h"

typedef enum {
    SUCCESS=0,
    BAD_ALLOC=1,
    BAD_FILE=2,
    NOT_IMPLEMENTED=3,
    INTERNAL_ASSERT=4,
    UNDEFINED_BEHAVIOUR=5,
    BAD_STRING=6,
    OUT_OF_RANGE=7,
    IO_ERROR=8,
    MAX_LOOP_LIMIT_HIT=9,
    SYNTAX_ERROR=10
} ERROR_CODES;

void * safe_malloc(size_t size);
void * safe_calloc(size_t nitems, size_t size);
FILE * safe_fopen(const char *filename, const char *mode);
char * safe_strdup( const char *str1 );
long int safe_strtol (const char* str, char** endptr, int base);

#endif
