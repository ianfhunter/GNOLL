
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include "shared_header.h"

// extern unsigned int MAX_SYMBOL_TEXT_LENGTH;

void concat_symbols(char ** arr1, int len1, char ** arr2, int len2, char ** new_arr){
    for(int i = 0; i != len1; i++){
        strcpy(new_arr[i], arr1[i]);
    }
    for(int i = 0; i != len2; i++){
        strcpy(new_arr[len1+i], arr2[i]);
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
    return -1;  // Not implemented
}


void collapse_vector(vec * vector, vec * new_vector){
    // Converts the like of "2d3"
    // from {1,2,3} to {6}
    // cannot operate on symbols.
    
    if (vector->dtype == SYMBOLIC ){
        new_vector = vector;
    }else{
        int c = 0;
        for(int i = 0; i != vector->length; i++){
            c += vector->content[i];
        }

        new_vector->content = calloc(sizeof(int), 1);
        new_vector->content[0] = c;
        new_vector->length = 1;
        new_vector->dtype = vector->dtype;
    }
}

unsigned int keep_logic(vec * vector, vec * new_vector, unsigned int number_to_keep, int keep_high){
    if (vector->dtype == SYMBOLIC){
        printf("Symbolic Dice, Cannot determine value. Consider using filters instead");
        return 1;
    }
    int available_amount = vector->length;
    if(available_amount > number_to_keep){
        new_vector->content = calloc(sizeof(int), number_to_keep);
        new_vector->length = number_to_keep;

        int * arr = vector->content;
        int * new_arr;
        int length = vector->length;

        for(int i = 0; i != number_to_keep; i++){
            int m;
            if (keep_high){
                m =  max(arr, length);
            }else{
                m =  min(arr, length);
            }
            new_vector->content[i] = m;
            new_arr = calloc(sizeof(int), length-1 );
            pop(arr, length, m, new_arr);
            free(arr);
            arr = new_arr;
            length -= 1;
        }
        new_vector->dtype = vector->dtype;
    }else{
        // e.g. 2d20k4 / 2d20kh2
        printf("Warning: KeepHighest: Keeping <= produced amount");
        new_vector = vector;
    }
    return 0;
}

unsigned int keep_lowest_values(vec * vector, vec * new_vector, unsigned int number_to_keep){
    return keep_logic(vector, new_vector, number_to_keep, 0);
}
unsigned int keep_highest_values(vec * vector, vec * new_vector, unsigned int number_to_keep){
    return keep_logic(vector, new_vector, number_to_keep, 1);
}