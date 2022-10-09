#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <errno.h>
#include "shared_header.h"
#include "safe_functions.h"

unsigned int gnoll_errno = 0;

void * safe_malloc(size_t size){
    void * malloc_result;
    malloc_result = malloc(size);
    if(!malloc_result){
        gnoll_errno = BAD_ALLOC;
    }
    return malloc_result;
}

void * safe_calloc(size_t nitems, size_t size){
    void * calloc_result;
    calloc_result = calloc(nitems, size);
    if(!calloc_result){
        gnoll_errno = BAD_ALLOC;
    }
    return calloc_result;
}

FILE * safe_fopen(const char *filename, const char *mode){
    FILE * fopen_result;
    fopen_result = fopen(filename, mode);
    if(fopen_result == NULL){
        printf("err opening\n");
        perror(filename);
        gnoll_errno = BAD_FILE;
    }
    return fopen_result;
}

int safe_fclose(FILE *stream){
    if(fclose(stream) != 0){
        printf("err closing\n");
        gnoll_errno = BAD_FILE;
    }
    return 0;
}

char * safe_strdup( const char *str1 ){
    char * result;
    unsigned int l = strlen(str1);
    result = safe_calloc(sizeof(char), l);
    result = strcpy(result, str1);
    if(result != 0){
        gnoll_errno = BAD_STRING;
    }
    return result;
}

long int safe_strtol (const char* str, char** endptr, int base){
    long int result;
    result = strtol(str,endptr,base);
    if(errno == ERANGE){
        gnoll_errno = OUT_OF_RANGE;
    }
    return result;
}

void safe_printf(const char *fmt, ...) {
    va_list args;
    va_start(args, fmt);
    int count = vprintf(fmt, args);
    va_end(args);
    if(count < 0) gnoll_errno = IO_ERROR;
}

void safe_fprintf(FILE *stream, const char *fmt, ...) {
    va_list args;
    va_start(args, fmt);
    int count = vfprintf(stream, fmt, args);
    va_end(args);
    if(count < 0) gnoll_errno = IO_ERROR;
}
