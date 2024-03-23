#ifndef __SAFE_FNS_H__
#define __SAFE_FNS_H__

#include <stdio.h>
#include <stdlib.h>

#include "shared_header.h"

typedef enum {
  SUCCESS = 0,
  BAD_ALLOC = 1,
  BAD_FILE = 2,
  NOT_IMPLEMENTED = 3,
  INTERNAL_ASSERT = 4,
  UNDEFINED_BEHAVIOUR = 5,
  BAD_STRING = 6,
  OUT_OF_RANGE = 7,
  IO_ERROR = 8,
  MAX_LOOP_LIMIT_HIT = 9,
  SYNTAX_ERROR = 10,
  DIVIDE_BY_ZERO = 11,
  UNDEFINED_MACRO = 12
} ERROR_CODES;

void print_gnoll_errors(void);
void *safe_malloc(size_t size);
void *safe_calloc(size_t nitems, size_t size);
FILE *safe_fopen(const char *filename, const char *mode);
char *safe_strdup(const char *str1);
long int safe_strtol(const char *str, char **endptr, int base);

void safe_copy_2d_chararray_with_allocation(char ***dst, char **src,
                                            unsigned int items,
                                            unsigned int max_size);
void free_2d_array(char ***arr, unsigned int items);

void free_vector(vec v);

long long fast_atoi(const char *str);

#endif
