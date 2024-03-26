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
  UNDEFINED_MACRO = 12,
  MATH_OVERFLOW = 13,
  MATH_UNDERFLOW = 14
} ERROR_CODES;

long long safe_subtract(long long a, long long b);
long long safe_add(long long a, long long b);
long long safe_mul(long long a, long long b);

void print_gnoll_errors(void);
void *safe_malloc(unsigned long long size);
void *safe_calloc(unsigned long long nitems, unsigned long long size);
FILE *safe_fopen(const char *filename, const char *mode);
char *safe_strdup(const char *str1);
long long int safe_strtol(const char *str, char **endptr, int base);

void safe_copy_2d_chararray_with_allocation(char ***dst, char **src,
                                            unsigned long long items,
                                            unsigned long long max_size);
void free_2d_array(char ***arr, unsigned long long items);

void free_vector(vec v);

long long fast_atoi(const char *str);

#endif
