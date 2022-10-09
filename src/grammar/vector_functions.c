#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include "shared_header.h"
#include "rolls/condition_checking.h"

#define MAX_SYMBOL_LENGTH 256

void initialize_vector(vec * vector, DIE_TYPE dt, int items){
    vector->dtype = dt;
    vector->length = items;

    if (dt == NUMERIC){
        vector->content = calloc(items, sizeof (int));
        if(! vector->content){
            exit(BAD_ALLOC);
        }
    }
    else if (dt == SYMBOLIC){
        vector->symbols = calloc(items, sizeof(char *));
        if(! vector->content){
            return BAD_ALLOC;
        }

        for (int i=0; i<items; i++){
            vector->symbols[i] = calloc(MAX_SYMBOL_LENGTH, sizeof (char));
            if(! vector->content){
                exit(BAD_ALLOC);
            }
        }
    }
}

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
    int seen = 0;
    
    for(int i = 0; i != len; i++){
        if (arr[i] == value && !seen){
            seen = 1;
            // Don't insert into new area.
        }
        else if(seen){
            new_arr[i-1] = arr[i];
        }else{
            new_arr[i] = arr[i];
        }
    }
}

int contains(int * arr, int len, int value){
    for(int i = 0; i != len; i++){
        if (arr[i] == value) return 1;
    }
    return 0;
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
    exit(NOT_IMPLEMENTED); 
    return 1;
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
        if(! new_vector->content){
            exit(BAD_ALLOC);
        }
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
        if(! new_vector->content){
            exit(BAD_ALLOC);
        }
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
            if(! vector->content){
                exit(BAD_ALLOC);
            }
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
unsigned int drop_lowest_values(vec * vector, vec * new_vector, unsigned int number_to_keep){
    int calc_keep = vector->length - number_to_keep;
    if (calc_keep > 0){
        number_to_keep = calc_keep;
    }else{
        number_to_keep = vector->length;
    }
    return keep_logic(vector, new_vector, number_to_keep, 1);
}
unsigned int drop_highest_values(vec * vector, vec * new_vector, unsigned int number_to_keep){
    int calc_keep = vector->length - number_to_keep;
    if (calc_keep > 0){
        number_to_keep = calc_keep;
    }else{
        number_to_keep = vector->length;
    }
    return keep_logic(vector, new_vector, number_to_keep, 0);
}

void extract_symbols(char ** symbols_list, char ** result_symbols, int * indexes, int idx_length){
    int index = 0;
    for (int i = 0; i != idx_length;i++){
        index = indexes[i];
        strcpy(result_symbols[i], symbols_list[index]);
    }

}

void filter(vec * dice, vec * cond, int comp_op, vec * output){
    int success_idx = 0;
    for(int i = 0; i != dice->length; i++){
        int v = dice->content[i];
        int compare_to = cond->content[0];
        // TODO: Non-First value
        // printf("%i == %i\n", v, compare_to);

        if(check_condition_scalar(v, compare_to, comp_op)){
            output->content[success_idx] = v;
            success_idx++;
        }
    }
    output->length = success_idx;
}

void filter_unique(vec * dice, vec * new_vec){
    int tracker_idx = 0;
    for(int i = 0; i != dice->length; i++){

        int v = dice->content[i];

        if(! contains(new_vec->content, new_vec->length, v)){
            new_vec->content[tracker_idx] = v;
            tracker_idx++;
        }
    }
    new_vec->length = tracker_idx;
}
