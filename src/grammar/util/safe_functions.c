#include "util/safe_functions.h"

#include <errno.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#include "shared_header.h"

int gnoll_errno = 0;
extern int verbose;


#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_RESET   "\x1b[0m"

long long safe_add(long long a, long long b){
    /* 
    A wrapper around addition to catch and signal over/underflow 
    Credit: https://stackoverflow.com/a/1514309/1421555
    */
    if (a > 0 && b > LLONG_MAX - a) {
      gnoll_errno = MATH_OVERFLOW;
      return LLONG_MAX;
    } else if (a < 0 && b < LLONG_MIN - a) {
      gnoll_errno = MATH_UNDERFLOW;
      return LLONG_MIN;
    }
    return a + b;
}


long long safe_subtract(long long a, long long b){
    /* 
    A wrapper around addition to catch and signal over/underflow 
    Credit: https://stackoverflow.com/a/1514309/1421555
    */
    if ((b < 0 && a > LLONG_MAX + b)) {
      gnoll_errno = MATH_OVERFLOW;
      return LLONG_MAX;
    } else if (b > 0 && a < LLONG_MIN + b) {
      gnoll_errno = MATH_UNDERFLOW;
      return LLONG_MIN;
    }
    return a - b;
}


long long safe_mul(long long a, long long b){
    /* 
    A wrapper around addition to catch and signal over/underflow 
    Credit: https://stackoverflow.com/a/1514309/1421555
    */
    if (b != 0 && a > LLONG_MAX / b) {
      gnoll_errno = MATH_OVERFLOW;
      return LLONG_MAX;
    } else if (b != 0 && a < LLONG_MAX / b) {
      gnoll_errno = MATH_UNDERFLOW;
      return LLONG_MIN;
    }
    return a * b;
}


void print_gnoll_errors(void){
  /**
   * @brief A human-readable translation of the gnoll error codes
   * 
   */
    switch(gnoll_errno){
      case SUCCESS:{
        if(verbose){
          printf("%sErrorCheck: No Errors.%s\n",ANSI_COLOR_GREEN, ANSI_COLOR_RESET);
        }
        break;
      }
      case BAD_ALLOC:{
        printf("%sErrorCheck: Bad Allocation.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case BAD_FILE:{
        printf("%sErrorCheck: Bad File.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case NOT_IMPLEMENTED:{
        printf("%sErrorCheck: Not Implemented.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case INTERNAL_ASSERT:{
        printf("%sErrorCheck: Internal Assertion.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case UNDEFINED_BEHAVIOUR:{
        printf("%sErrorCheck: Undefined Behaviour.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case BAD_STRING:{
        printf("%sErrorCheck: Bad String.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case OUT_OF_RANGE:{
        printf("%sErrorCheck: Out of Range.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case IO_ERROR:{
        printf("%sErrorCheck: I/O Error.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case MAX_LOOP_LIMIT_HIT:{
        printf("%sErrorCheck: Max Loop Limit Reached.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case SYNTAX_ERROR:{
        printf("%sErrorCheck: Syntax Error.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case DIVIDE_BY_ZERO:{
        printf("%sErrorCheck: Divide by Zero.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case UNDEFINED_MACRO:{
        printf("%sErrorCheck: Undefined Macro.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case MATH_OVERFLOW:{
        printf("%sErrorCheck: Math overflow/saturation.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      case MATH_UNDERFLOW:{
        printf("%sErrorCheck: Math underflow/desaturation.%s\n",ANSI_COLOR_RED, ANSI_COLOR_RESET);
        break;
      }
      default:{
        printf("%sErrorCheck: Error (Undetermined. Code %i).%s\n",ANSI_COLOR_RED, gnoll_errno, ANSI_COLOR_RESET);
        break;
      }
  }
}

void *safe_malloc(unsigned long long size) {
  /**
   * @brief Safe version of malloc. Populates gnoll_errno on error
   * @param size
   * @return
   */

  if (gnoll_errno) {
    // If there was already an error,
    // Don't even try to execute.
    return NULL;
  }
  void *malloc_result;
  malloc_result = malloc(size);
  if (!malloc_result && size) {
    gnoll_errno = BAD_ALLOC;
  }
  return malloc_result;
}

void free_vector(vec v){
  if(v.dtype == NUMERIC){
    free(v.storage.content);
  }else{
    free_2d_array(&v.storage.symbols, v.length);
    if (v.has_source){
      // Should be always the same as length (But not sure that's true!)
      free_2d_array(&v.source.symbol_pool, v.source.die_sides);
    }
  }
}

void free_2d_array(char ***arr, unsigned long long items) {
  /**
   * @brief Free a 2d char array in a repeatable manner.
   * @param arr
   * @param items
   */
  if (*arr) {
    for (unsigned long long i = 0; i != items; i++) {
      if ((*arr)[i]) {
        free((*arr)[i]);
      }
    }
    free(*arr);
  }
}

void safe_copy_2d_chararray_with_allocation(char ***dst, char **src,
                                            unsigned long long items,
                                            unsigned long long max_size) {
  /**
   * @brief Copy from one 2d char array to another in a repeatable manner.
   * @param dst
   * @param src
   * @param item
   * @param max_size
   */

  *dst = (char**)safe_calloc(items, sizeof(char **));
  if (gnoll_errno) {
    return;
  }

  for (unsigned long long i = 0; i != items; i++) {
    
    (*dst)[i] = (char*)safe_calloc(sizeof(char), max_size);
    if (gnoll_errno) {
      return;
    }
    
    memcpy((*dst)[i], src[i], max_size);
  }
  
}

void * safe_calloc(unsigned long long nitems, unsigned long long size) {
  /**
   * @brief Safe version of calloc. Populates gnoll_errno on error
   * @param size
   * @return
   */
  if (gnoll_errno) {
    // If there was already an error,
    // Don't even try to execute.
    return NULL;
  }
  void *calloc_result = NULL;
  calloc_result = calloc(nitems, size);
  unsigned long long total_sz = nitems * size;
  if (!calloc_result && total_sz) {
    gnoll_errno = BAD_ALLOC;
  }
  return calloc_result;
}

FILE *safe_fopen(const char *filename, const char *mode) {
  /**
   * @brief Safe version of fopen. Populates gnoll_errno on error
   * @param size
   * @return
   */
  if (gnoll_errno) {
    // If there was already an error,
    // Don't even try to execute.
    return NULL;
  }
  FILE *fopen_result;
  fopen_result = fopen(filename, mode);
  if (fopen_result == NULL) {
    printf("err opening\n");
    perror(filename);
    gnoll_errno = BAD_FILE;
  }
  return fopen_result;
}

char *safe_strdup(const char *str1) {
  /**
   * @brief Safe version of strdup. Populates gnoll_errno on error
   * @param str1
   * @return
   */
  if (gnoll_errno) {
    // If there was already an error,
    // Don't even try to execute.
    return NULL;
  }
  char *result;
  // unsigned int l = strlen(str1) + 1;  //+1 for \0
  result = (char*) safe_calloc(sizeof(char), MAX_SYMBOL_LENGTH);
  // result = (char*) safe_calloc(sizeof(char), l);
  result = strcpy(result, str1);
  if (result == 0) {
    gnoll_errno = BAD_STRING;
  }
  return result;
}

long long fast_atoi(const char *str) {
  /**
   * @brief Safe version of atoi. Populates gnoll_errno on error
   * @param str
   * @return
   */
  // Ref: https://stackoverflow.com/a/16826908/1421555
  long long val = 0;
  while (*str) {
    val = val * 10 + (*str++ - '0');
  }
  return val;
}

long long safe_strtol(const char *str, char **endptr, int base) {
  /**
   * @brief Safe version of strtol. Populates gnoll_errno on error
   * @param str
   * @param endptr
   * @param base
   * @return
   */
  if (gnoll_errno) {
    return 0;
  }
  long long result;
  result = strtol(str, endptr, base);
  if (errno == ERANGE) {
    gnoll_errno = OUT_OF_RANGE;
  }
  return result;
}
