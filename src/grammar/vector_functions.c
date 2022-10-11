#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include "vector_functions.h"
#include "shared_header.h"
#include "safe_functions.h"
#include "rolls/condition_checking.h"

#define MAX_SYMBOL_LENGTH 256
extern int gnoll_errno;

void initialize_vector(vec * vector, DIE_TYPE dt, unsigned int number_of_items){
    if (gnoll_errno){ return ; }
    
    vector->dtype = dt;
    vector->length = items;

    if (dt == NUMERIC){
        vector->content = safe_calloc(items, sizeof (int));
        if(gnoll_errno) return;
    }
    else if (dt == SYMBOLIC){
        vector->symbols = safe_calloc(items, sizeof(char *));
        if(gnoll_errno) return;

        for (int i=0; i<items; i++){
            vector->symbols[i] = safe_calloc(MAX_SYMBOL_LENGTH, sizeof (char));
            if(gnoll_errno) return;
        }
    }
}

void concat_symbols(char ** arr1, int len1, char ** arr2, int len2, char ** new_arr){
    if (gnoll_errno){ return ; }

    for(int i = 0; i != len1; i++){
        strcpy(new_arr[i], arr1[i]);
    }
    for(int i = 0; i != len2; i++){
        strcpy(new_arr[len1+i], arr2[i]);
    }
}

void pop(int * arr, int len, int value, int * new_arr){
    if (gnoll_errno){ return ; }

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
    if (gnoll_errno){ return 0; }

    for(int i = 0; i != len; i++){
        if (arr[i] == value) return 1;
    }
    return 0;
}

int min(int * arr, int len){
    if (gnoll_errno){ return 0; }

    int lowest = INT_MAX;
    for(int i = 0; i != len; i++){
        if (arr[i] < lowest) lowest = arr[i];
    }
    return lowest;
}

int max(int * arr, int len){
    if (gnoll_errno){ return 0; }

    int highest = INT_MIN;
    for(int i = 0; i != len; i++){
        if (arr[i] > highest) highest = arr[i];
    }
    return highest;
}

void print_vec(vec vector){
    if (gnoll_errno){ return ; }

    safe_printf("Vector Size: %d\n", vector.length);
    safe_printf("Vector Type: %d\n", vector.dtype);
    if(vector.dtype == NUMERIC){
        safe_printf("Content:\n");
        for(int i = 0; i != vector.length; i++){
            safe_printf(" %d\n", vector.content[i]);
        }
    }else{
        safe_printf("Symbols:\n");
        for(int i = 0; i != vector.length; i++){
            safe_printf(" %c\n", vector.symbols[i][0]);
        }
    }
}

unsigned int remove_if_present(char ** arr1, int len1,
                    char ** arr2, int len2,
                    char ** new_arr)
{
    if (gnoll_errno){ return 0; }

    gnoll_errno = NOT_IMPLEMENTED; 
    return 1;
}


void collapse_vector(vec * vector, vec * new_vector){
    // Converts the like of "2d3"
    // from {1,2,3} to {6}
    // cannot operate on symbols.
    if (gnoll_errno){ return ; }

    if (vector->dtype == SYMBOLIC ){
        new_vector = vector;
    }else{
        int c = 0;
        for(int i = 0; i != vector->length; i++){
            c += vector->content[i];
        }

        new_vector->content = safe_calloc(sizeof(int), 1);
        if(gnoll_errno) return;
        new_vector->content[0] = c;
        new_vector->length = 1;
        new_vector->dtype = vector->dtype;
    }
}

unsigned int keep_logic(vec * vector, vec * new_vector, unsigned int number_to_keep, int keep_high){
    if (gnoll_errno){ return 0; }

    if (vector->dtype == SYMBOLIC){
        safe_printf("Symbolic Dice, Cannot determine value. Consider using filters instead");
        gnoll_errno = UNDEFINED_BEHAVIOUR;
        return 0;
    }
    int available_amount = vector->length;
    if(available_amount > number_to_keep){
        new_vector->content = safe_calloc(sizeof(int), number_to_keep);
        if(gnoll_errno) return 0;
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
            new_arr = safe_calloc(sizeof(int), length-1 );
            if(gnoll_errno) return 0;

            pop(arr, length, m, new_arr);
            free(arr);
            arr = new_arr;
            length -= 1;
        }
        new_vector->dtype = vector->dtype;
    }else{
        // e.g. 2d20k4 / 2d20kh2
        safe_printf("Warning: KeepHighest: Keeping <= produced amount");
        new_vector = vector;
    }
    return 0;
}

unsigned int keep_lowest_values(vec * vector, vec * new_vector, unsigned int number_to_keep){
    if (gnoll_errno){ return 0; }

    return keep_logic(vector, new_vector, number_to_keep, 0);
}
unsigned int keep_highest_values(vec * vector, vec * new_vector, unsigned int number_to_keep){
    if (gnoll_errno){ return 0; }

    return keep_logic(vector, new_vector, number_to_keep, 1);
}
unsigned int drop_lowest_values(vec * vector, vec * new_vector, unsigned int number_to_keep){
    if (gnoll_errno){ return 0; }

    int calc_keep = vector->length - number_to_keep;
    if (calc_keep > 0){
        number_to_keep = calc_keep;
    }else{
        number_to_keep = vector->length;
    }
    return keep_logic(vector, new_vector, number_to_keep, 1);
}
unsigned int drop_highest_values(vec * vector, vec * new_vector, unsigned int number_to_keep){
    if (gnoll_errno){ return 0; }

    int calc_keep = vector->length - number_to_keep;
    if (calc_keep > 0){
        number_to_keep = calc_keep;
    }else{
        number_to_keep = vector->length;
    }
    return keep_logic(vector, new_vector, number_to_keep, 0);
}

void extract_symbols(char ** symbols_list, char ** result_symbols, int * indexes, int idx_length){
    if (gnoll_errno){ return ; }

    int index = 0;
    for (int i = 0; i != idx_length;i++){
        index = indexes[i];
        strcpy(result_symbols[i], symbols_list[index]);
    }
}

void filter(vec * dice, vec * cond, int comp_op, vec * output){
    if (gnoll_errno){ return ; }

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
    if (gnoll_errno){ return ; }

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
