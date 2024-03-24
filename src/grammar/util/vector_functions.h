#ifndef VECFN_HEADER
#define VECFN_HEADER

#include "constructs/dice_enums.h"
#include "constructs/vec.h"
#include "shared_header.h"
#include <stdbool.h>


void initialize_vector_pointer(vec ***vector, DIE_TYPE dt, unsigned long long number_of_items);
void initialize_vector(vec* vector, DIE_TYPE dt, unsigned long long number_of_items);

void light_initialize_vector(vec* vector, DIE_TYPE dt,
                             unsigned long long number_of_items);

void pop(long long* arr, unsigned long long len, int value, long long* new_arr);

void abs_vec(vec* x);

int contains(long long* arr, unsigned long long len, long long value);
int min_in_vec(long long* arr, unsigned long long len);
int max_in_vec(long long* arr, unsigned long long len);

void concat_symbols(char** arr1, unsigned long long len1, char** arr2,
                    unsigned long long len2, char** new_arr);

void collapse_vector(vec* vector, vec* new_vector);


void keep_logic(vec* vector, vec** new_vector, unsigned long long umber_to_keep,
                bool keep_high);
void keep_highest_values(vec* vector, vec** new_vector,
                         unsigned long long number_to_keep);
void keep_lowest_values(vec* vector, vec** new_vector,
                        unsigned long long number_to_keep);
void drop_highest_values(vec* vector, vec** new_vector,
                         unsigned long long number_to_drop);
void drop_lowest_values(vec* vector, vec** new_vector,
                        unsigned long long number_to_drop);


void extract_symbols(char** symbols_list, char** result_symbols, long long* indexes,
                     unsigned long long idx_length);

void print_vec(vec vector);

void filter(vec* dice, vec* cond, int comparitor, vec* output);

void filter_unique(vec* dice, vec* new_vec);

#endif
