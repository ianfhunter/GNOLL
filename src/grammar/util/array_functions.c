
#include "util/array_functions.h"

long long collapse(long long * arr, unsigned long long len){
    return sum(arr, len);
}

long long sum(long long * arr, unsigned long long len){
    long long result = 0;
    for(unsigned long long i = 0; i != len; i++) result += arr[i];
    return result;
}
