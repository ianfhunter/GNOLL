#ifndef VECFN_HEADER
#define VECFN_HEADER
#include "shared_header.h"

void initialize_vector(vec * vector, DIE_TYPE dt, int num);

void pop(int * arr, int len, int value, int * new_arr);

int min(int * arr, int len);
int max(int * arr, int len);

void concat_symbols(char ** arr1, int len1,
                    char ** arr2, int len2,
                    char ** new_arr);

unsigned int remove_if_present(char ** arr1, int len1,
                    char ** arr2, int len2,
                    char ** new_arr);

void collapse_vector(vec * vector, vec * new_vector);

unsigned int keep_highest_values(vec * vector, vec * new_vector, unsigned int number_to_keep);
unsigned int keep_lowest_values(vec * vector, vec * new_vector, unsigned int number_to_keep);
// unsigned int keep_logic(vec * vector, vec * new_vector, unsigned int number_to_keep, int keep_high);

void extract_symbols(char ** symbols_list, char ** result_symbols, int * indexes, int idx_length);

void print_vec(vec vector);
#endif