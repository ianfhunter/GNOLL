
#include "util/array_functions.h"

int collapse(int * arr, unsigned int len){
    return sum(arr, len);
}

int sum(int * arr, unsigned int len){
    int result = 0;
    for(unsigned int i = 0; i != len; i++) result += arr[i];
    return result;
}