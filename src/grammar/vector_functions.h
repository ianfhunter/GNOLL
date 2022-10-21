#ifndef VECFN_HEADER
#define VECFN_HEADER

#include "shared_header.h"
#include "rolls/dice_enums.h"
#include "rolls/vec.h"

void initialize_vector(vec * vector, DIE_TYPE dt, unsigned int number_of_items);
void light_initialize_vector(vec * vector, DIE_TYPE dt, unsigned int number_of_items);

void pop(int * arr, unsigned int len, int value, int * new_arr);

int contains(int * arr, unsigned int len, int value);
int min(int * arr, unsigned int len);
int max(int * arr, unsigned int len);

void concat_symbols(char ** arr1, unsigned int len1,
                    char ** arr2, unsigned int len2,
                    char ** new_arr);

unsigned int remove_if_present(char ** arr1, unsigned int len1,
                    char ** arr2, unsigned int len2,
                    char ** new_arr);

void collapse_vector(vec * vector, vec * new_vector);

unsigned int keep_logic(vec * vector, vec * new_vector, unsigned int number_to_keep, int keep_high);
unsigned int keep_highest_values(vec * vector, vec * new_vector, unsigned int number_to_keep);
unsigned int keep_lowest_values(vec * vector, vec * new_vector, unsigned int number_to_keep);
unsigned int drop_highest_values(vec * vector, vec * new_vector, unsigned int number_to_keep);
unsigned int drop_lowest_values(vec * vector, vec * new_vector, unsigned int number_to_keep);

void extract_symbols(char ** symbols_list, char ** result_symbols, int * indexes, unsigned int idx_length);

void print_vec(vec vector);

void filter(vec * dice, vec * cond, int comparitor, vec * output);

void filter_unique(vec * dice, vec * new_vec);

#endif
