
#include "util/array_functions.h"

int collapse(int * arr, unsigned long long len){
    return sum(arr, len);
}

int sum(int * arr, unsigned long long len){
    int result = 0;
    for(unsigned long long i = 0; i != len; i++) result += arr[i];
    return result;
}
