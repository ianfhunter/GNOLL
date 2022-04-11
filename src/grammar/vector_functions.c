
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include "shared_header.h"

void concat_symbols(char ** arr1, int len1, char ** arr2, int len2, char ** new_arr){
    for(int i = 0; i != len1; i++){
        new_arr[i][0] = arr1[i][0];
    }
    for(int i = 0; i != len2; i++){
        new_arr[len1+i][0] = arr2[i][0];
    }
}

void pop(int * arr, int len, int value, int * new_arr){
    // This could be done in-place.
    bool seen = false;
    // new_arr = calloc(sizeof(int), (len-1));

    for(int i = 0; i != len; i++){
        if (arr[i] == value && !seen){
            seen = true;
            // Don't insert into new area.
        }
        else if(seen){
            new_arr[i-1] = arr[i];
        }else{
            new_arr[i] = arr[i];
        }
    }
}

int min(int * arr, int len){
    int lowest = INT_MAX;
    for(int i = 0; i != len; i++){
        if (arr[i] < lowest) lowest = arr[i];
    }
    return lowest;
}
int max(int * arr, int len){
    int highest = INT_MIN;
    for(int i = 0; i != len; i++){
        if (arr[i] > highest) highest = arr[i];
    }
    return highest;
}
void print_vec(vec vector){
    printf("Vector Size: %d\n", vector.length);
    printf("Vector Type: %d\n", vector.dtype);
    if(vector.dtype == NUMERIC){
        printf("Content:\n");
        for(int i = 0; i != vector.length; i++){
            printf(" %d\n", vector.content[i]);
        }
    }else{
        printf("Symbols:\n");
        for(int i = 0; i != vector.length; i++){
            printf(" %c\n", vector.symbols[i][0]);
        }
    }
}


unsigned int remove_if_present(char ** arr1, int len1,
                    char ** arr2, int len2,
                    char ** new_arr)
{
    for(int i = 0; i != len1; i++){
        for(int j = 0; j != len2; j++){
            // if arr1[i] in arr2
            //      pop(arr2)
            // else
            //      new_arr = i

        }
    }
}
