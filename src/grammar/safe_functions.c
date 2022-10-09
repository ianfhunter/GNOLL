#include <stdio.h>
#include <stdlib.h>
#include "shared_header.h"

void * safe_malloc(size_t size){
    void * malloc_result;
    malloc_result = malloc(size);
    if(!malloc_result){
        exit(BAD_ALLOC);
    }
    return malloc_result;
}

void * safe_calloc(size_t nitems, size_t size){
    void * calloc_result;
    calloc_result = calloc(nitems, size);
    if(!calloc_result){
        exit(BAD_ALLOC);
    }
    return calloc_result;
}
FILE * safe_fopen(const char *filename, const char *mode){
    FILE * fopen_result;
    fopen_result = fopen(filename, mode);
    if(!fopen_result){
        exit(BAD_FILE);
    }
    return fopen_result;
}
