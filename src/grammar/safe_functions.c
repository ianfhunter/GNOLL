#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <errno.h>
#include "shared_header.h"
#include "safe_functions.h"

int gnoll_errno = 0;

void * safe_malloc(size_t size){
    if (gnoll_errno){
        // If there was already an error,
        // Don't even try to execute.
        return NULL;
    }
    void * malloc_result;
    malloc_result = malloc(size);
    if(!malloc_result && size){
        gnoll_errno = BAD_ALLOC;
    }
    return malloc_result;
}

void free_2d_array(char ***arr, unsigned int items){
    // printf("Try to free: %p\n",*arr);
    if (*arr){
        for(unsigned int i = 0; i != items; i++){
            // printf("[%u] Try to free: %p\n",i, (*arr)[i]);
            if ((*arr)[i]){
                free((*arr)[i]);
            }
        }
        free(*arr);
    }
}

void safe_copy_2d_chararray_with_allocation(
    char *** dst, 
    char ** src, 
    unsigned int items, 
    unsigned int max_size)
{
    *dst = safe_calloc(items, sizeof(char **));
    if(gnoll_errno){return;}
    // printf("memcpy %p <- %p (%u)\n", *dst, src, items);
    for(unsigned int i = 0; i!=items; i++){
        (*dst)[i] = safe_calloc(sizeof(char), max_size);
        if(gnoll_errno){return;}
        // printf("---memcpy %p <- %p (%u)[%s]\n", (*dst)[i], src[i], max_size, src[i]);
        memcpy((*dst)[i], src[i], max_size);
        // printf("1 Debug %p %s\n", (*dst)[i], (*dst)[i]);
    }
}

void * safe_calloc(size_t nitems, size_t size){
    if (gnoll_errno){
        // If there was already an error,
        // Don't even try to execute.
        return NULL;
    }
    void * calloc_result;
    calloc_result = calloc(nitems, size);
    unsigned int total_sz = nitems*size;
    if(!calloc_result && total_sz){
        gnoll_errno = BAD_ALLOC;
    }
    return calloc_result;
}

FILE * safe_fopen(const char *filename, const char *mode){
    if (gnoll_errno){
        // If there was already an error,
        // Don't even try to execute.
        return NULL;
    }
    FILE * fopen_result;
    fopen_result = fopen(filename, mode);
    if(fopen_result == NULL){
        printf("err opening\n");
        perror(filename);
        gnoll_errno = BAD_FILE;
    }
    return fopen_result;
}

char * safe_strdup( const char *str1 ){
    if (gnoll_errno){
        // If there was already an error,
        // Don't even try to execute.
        return NULL;
    }
    char * result;
    unsigned int l = strlen(str1) + 1;  //+1 for \0
    result = safe_calloc(sizeof(char), l);
    result = strcpy(result, str1);
    if(result == 0){
        gnoll_errno = BAD_STRING;
    }
    return result;
}

int fast_atoi( const char * str )
{
    //Ref: https://stackoverflow.com/a/16826908/1421555
    int val = 0;
    while( *str ) {
        val = val*10 + (*str++ - '0');
    }
    return val;
}

long int safe_strtol (const char* str, char** endptr, int base){
    if (gnoll_errno){
        // If there was already an error,
        // Don't even try to execute.
        return 0;
    }
    long int result;
    result = strtol(str,endptr,base);
    if(errno == ERANGE){
        gnoll_errno = OUT_OF_RANGE;
    }
    return result;
}
