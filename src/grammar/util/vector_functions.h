#ifndef VECFN_HEADER
#define VECFN_HEADER

#include "constructs/dice_enums.h"
#include "constructs/vec.h"
#include "shared_header.h"

void initialize_vector(vec* vector, DIE_TYPE dt, unsigned int number_of_items);
void light_initialize_vector(vec* vector, DIE_TYPE dt,
                             unsigned int number_of_items);

void pop(int* arr, unsigned int len, int value, int* new_arr);

void abs_vec(vec* x);

int contains(int* arr, unsigned int len, int value);
int min_in_vec(int* arr, unsigned int len);
int max_in_vec(int* arr, unsigned int len);

void concat_symbols(char** arr1, unsigned int len1, char** arr2,
                    unsigned int len2, char** new_arr);

void collapse_vector(vec* vector, vec* new_vector);

void keep_logic(vec* vector, vec** new_vector, unsigned int number_to_keep,
                int keep_high);
void keep_highest_values(vec* vector, vec* new_vector,
                         unsigned int number_to_keep);
void keep_lowest_values(vec* vector, vec* new_vector,
                        unsigned int number_to_keep);
void drop_highest_values(vec* vector, vec* new_vector,
                         unsigned int number_to_keep);
void drop_lowest_values(vec* vector, vec* new_vector,
                        unsigned int number_to_keep);

void extract_symbols(char** symbols_list, char** result_symbols, int* indexes,
                     unsigned int idx_length);

void print_vec(vec vector);

void filter(vec* dice, vec* cond, int comparitor, vec* output);

void filter_unique(vec* dice, vec* new_vec);

#endif
