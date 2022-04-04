#ifndef VECFN_HEADER
#define VECFN_HEADER
#include "shared_header.h"

void pop(int * arr, int len, int value, int * new_arr);

int min(int * arr, int len);
int max(int * arr, int len);

void concat_symbols(char ** arr1, int len1,
                    char ** arr2, int len2,
                    char ** new_arr);

unsigned int remove_if_present(char ** arr1, int len1,
                    char ** arr2, int len2,
                    char ** new_arr);

void print_vec(vec vector);
#endif