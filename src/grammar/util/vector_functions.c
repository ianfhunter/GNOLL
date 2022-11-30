#include "util/vector_functions.h"

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "operations/conditionals.h"
#include "shared_header.h"
#include "util/safe_functions.h"
#include "shared_header.h"

extern int gnoll_errno;

void light_initialize_vector(vec *vector, DIE_TYPE dt,
                             unsigned int number_of_items) {
  /**
   * @brief Initializes a vector, but does not fill out 2d arrays
   * @param vector vector to initialize
   * @param dt dice type
   * @param number_of_items how many items in the arrays
   * @return
   */
  vector->dtype = dt;
  vector->length = number_of_items;
  vector->has_source = false;

  if (dt == NUMERIC) {
    vector->content = (int*)safe_calloc(number_of_items, sizeof(int));
    if (gnoll_errno) return;
  } else if (dt == SYMBOLIC) {
    vector->symbols = (char**)safe_calloc(1, sizeof(char **));
  }
}
void initialize_vector(vec *vector, DIE_TYPE dt, unsigned int number_of_items) {
  /**
   * @brief Initializes a vector, reserving space for 2d arrays
   * @param vector vector to initialize
   * @param dt dice type
   * @param number_of_items how many items in the arrays
   * @return
   */
  if (gnoll_errno) {
    return;
  }

  vector->dtype = dt;
  vector->length = number_of_items;
  vector->has_source = false;

  if (dt == NUMERIC) {
    vector->content = (int*)safe_calloc(number_of_items, sizeof(int));
    if (gnoll_errno) return;
  } 
  else if (dt == SYMBOLIC) 
  {
    vector->symbols = (char**)safe_calloc(number_of_items, sizeof(char *));
    if (gnoll_errno) return;

    for (unsigned int i = 0; i < number_of_items; i++) {
      vector->symbols[i] = (char*)safe_calloc(MAX_SYMBOL_LENGTH, sizeof(char));
      if (gnoll_errno) return;
    }
  }
}

void concat_symbols(char **arr1, unsigned int len1, char **arr2,
                    unsigned int len2, char **new_arr) {
  /**
   * @brief Concatenates two 2D arrays of dice symbols
   * @param arr1
   * @param len1
   * @param arr2
   * @param len2
   * @param new_arr
   * @return
   */
  if (gnoll_errno) {
    return;
  }

  for (unsigned int i = 0; i != len1; i++) {
    strcpy(new_arr[i], arr1[i]);
    // free(arr1[i]);
  }
  for (unsigned int i = 0; i != len2; i++) {
    unsigned int idx = len1 + i;
    strcpy(new_arr[idx], arr2[i]);
    // free(arr2[i]);
  }
}

void pop(int *arr, unsigned int len, int value, int *new_arr) {
  /**
   * @brief Removes a value from an array
   * @param arr
   * @param len
   * @param value
   * @param new_arr
   */
  if (gnoll_errno) {
    return;
  }

  // This could be done in-place.
  int seen = 0;

  for (unsigned int i = 0; i != len; i++) {
    if (arr[i] == value && !seen) {
      seen = 1;
      // Don't insert into new area.
    } else if (seen) {
      new_arr[i - 1] = arr[i];
    } else {
      new_arr[i] = arr[i];
    }
  }
}

int contains(int *arr, unsigned int len, int value) {
  /**
   * @brief Checks if a value exists in an array
   * @param arr
   * @param len
   * @param value
   * @return true or false (1 or 0)
   */
  if (gnoll_errno) {
    return 0;
  }

  for (unsigned int i = 0; i != len; i++) {
    if (arr[i] == value) return 1;
  }
  return 0;
}

int min_in_vec(int *arr, unsigned int len) {
  /**
   * @brief Return the smallest value from an array
   * @param arr
   * @param len
   * @return minimum value
   */
  if (gnoll_errno) {
    return 0;
  }

  int lowest = INT_MAX;
  for (unsigned int i = 0; i != len; i++) {
    if (arr[i] < lowest) lowest = arr[i];
  }
  return lowest;
}

int max_in_vec(int *arr, unsigned int len) {
  /**
   * @brief Return the biggest value in an array
   * @param arr
   * @param len
   * @return maximum value
   */
  if (gnoll_errno) {
    return 0;
  }

  int highest = INT_MIN;
  for (unsigned int i = 0; i != len; i++) {
    if (arr[i] > highest) highest = arr[i];
  }
  return highest;
}
void abs_vec(vec *x) {
  for (unsigned int i = 0; i != x->length; i++) {
    int v = x->content[i];
    if (v < 0) {
      x->content[i] *= -1;
    }
  }
}

void print_vec(vec vector) {
  /**
   * @brief Print information about a vec that may be interesting for debug
   * @param vec
   */
  if (gnoll_errno) {
    return;
  }

  printf("Vector Size: %u\n", vector.length);
  if (vector.dtype == NUMERIC) {
    printf("Vector Type: NUMERIC\n");
    for (unsigned int i = 0; i != vector.length; i++) {
      printf("\t%d\n", vector.content[i]);
    }
  } else {
    printf("Vector Type: SYMBOLIC\n");
    printf("Symbols:\n");
    for (unsigned int i = 0; i != vector.length; i++) {
      printf("\t- %s\n", vector.symbols[i]);
    }
  }
}

void collapse_vector(vec *vector, vec *new_vector) {
  /**
   * @brief Collapses multiple Numeric dice to one value by summing
   * @param vector source
   * @param new_vector dest
   */
  if (gnoll_errno) {
    return;
  }

  if (vector->dtype == SYMBOLIC) {
    safe_copy_2d_chararray_with_allocation(
       &new_vector->symbols,
       vector->symbols,
       vector->length,
       MAX_SYMBOL_LENGTH
    );
    
    new_vector->length = vector->length;
    new_vector->dtype = SYMBOLIC;
    new_vector->has_source = false;
  } 
  else {
    int c = 0;
    for (unsigned int i = 0; i != vector->length; i++) {
      c += vector->content[i];
    }

    new_vector->content = (int*)safe_calloc(sizeof(int), 1);
    if (gnoll_errno) return;
    new_vector->content[0] = c;
    new_vector->length = 1;
    new_vector->dtype = NUMERIC;
    new_vector->has_source = false;
  }
  return;
}

void keep_logic(vec *vector, vec *output_vector, unsigned int number_to_keep,
                int keep_high) {
  /**
   * @brief Collapses multiple Numeric dice to one value by summing
   * @param vector source (Freed at end)
   * @param output_vector dest
   * @param number_to_keep how many values to keep or drop
   * @param keep_high Whether to keep the highest (1) or Lowest (0) values
   */
  if (gnoll_errno) {
    return;
  }

  unsigned int available_amount = vector->length;

  if (vector->dtype == SYMBOLIC) {
    printf(
        "Symbolic Dice, Cannot determine value. Consider using filters "
        "instead");
    gnoll_errno = UNDEFINED_BEHAVIOUR;
    return;
  }
  
  if (available_amount > number_to_keep) {
    initialize_vector(output_vector, vector->dtype, number_to_keep);

    // output_vector->content = (int*)safe_calloc(sizeof(int), number_to_keep);
    // if (gnoll_errno) {
    //   return;
    // }
    // output_vector->length = number_to_keep;

    int *arr = vector->content;
    int *new_arr;
    unsigned int length = vector->length;

    // while (number needed)
    //     Get Max/Min from vector
    //     Store in output
    for (unsigned int i = 0; i != number_to_keep; i++) {
      int m;
      if (keep_high) {
        m = max_in_vec(arr, length);
      } else {
        m = min_in_vec(arr, length);
      }
      output_vector->content[i] = m;
      new_arr = (int*)safe_calloc(sizeof(int), length - 1);
      if (gnoll_errno) {
        return;
      }

      // Take 'm' out of the array (put in new_array)
      pop(arr, length, m, new_arr);
      free(arr);
      arr = new_arr;
      length -= 1;
    }
    free(arr);
    // output_vector->content = arr;
    output_vector->dtype = vector->dtype;
  } else {
    // e.g. 2d20k4 / 2d20kh2
    printf("Warning: KeepHighest: Keeping <= produced amount");
    output_vector = vector;
  }
}

void keep_lowest_values(vec *vector, vec *new_vector,
                        unsigned int number_to_keep) {
  /**
   * @brief Keep the lowest values from a set of dice
   */
  keep_logic(vector, new_vector, number_to_keep, 0);
}
void keep_highest_values(vec *vector, vec *new_vector,
                         unsigned int number_to_keep) {
  /**
   * @brief Keep the Highest values from a set of dice
   */
  keep_logic(vector, new_vector, number_to_keep, 1);
}
void drop_lowest_values(vec *vector, vec *new_vector,
                        unsigned int number_to_keep) {
  /**
   * @brief Drop the lowest values from a set of dice
   */
  int calc_keep = (int)vector->length - (int)number_to_keep;
  if (calc_keep > 0) {
    number_to_keep = (unsigned int)calc_keep;
  } else {
    number_to_keep = (unsigned int)vector->length;
  }
  keep_logic(vector, new_vector, number_to_keep, 1);
}
void drop_highest_values(vec *vector, vec *new_vector,
                         unsigned int number_to_keep) {
  /**
   * @brief Drop the highest values from a set of dice
   */

  int calc_keep = (int)vector->length - (int)number_to_keep;
  if (calc_keep > 0) {
    number_to_keep = (unsigned int)calc_keep;
  } else {
    number_to_keep = (unsigned int)vector->length;
  }
  keep_logic(vector, new_vector, number_to_keep, 0);
}

void extract_symbols(char **symbols_list, char **result_symbols, int *indexes,
                     unsigned int idx_length) {
  /**
   * @brief Take symbols from indexed locations in an array and save to a new
   * location
   * @param symbols_list List of symbols
   * @param result_symbols Output location
   * @param indexes List of symbol indexes to choose
   * @param idx_length How long is the `indexes` list
   */
  if (gnoll_errno) {
    return;
  }

  // Free up memory before overwriting (done in vec-init)
  for (unsigned int i = 0; i != idx_length; i++) {
    if (result_symbols[i]) {
      free(result_symbols[i]);
    }
  }

  for (unsigned int i = 0; i != idx_length; i++) {
    int index = indexes[i];
    result_symbols[i] = safe_strdup(symbols_list[index]);
  }
}

void filter(vec *dice, vec *cond, int comp_op, vec *output) {
  /**
   * @brief Keep dice that match a filter, discard otherwise
   * @param dice Dice vector
   * @param cond Values to compare to
   * @param comp_op Comparison Operation
   * @param output Output location
   */
  if (gnoll_errno) {
    return;
  }
  if (comp_op == IS_UNIQUE){
    filter_unique(dice, output);
    return;
  }

  unsigned int success_idx = 0;
  for (unsigned int i = 0; i != dice->length; i++) {
    int v = dice->content[i];
    if (comp_op == IF_EVEN || comp_op == IF_ODD){
      if(check_condition_scalar(v, v, (COMPARATOR)comp_op)){
        output->content[success_idx] = v;
        success_idx++;
      }
    }else{

      int compare_to = cond->content[0];

      if (check_condition_scalar(v, compare_to, (COMPARATOR)comp_op)) {
        output->content[success_idx] = v;
        success_idx++;
      }
    }
  }
  output->length = success_idx;
}

void filter_unique(vec *dice, vec *new_vec) {
  /**
   * @brief Keep dice that are unique, discard otherwise.
   * @param dice Dice vector
   * @param new_vec Output location
   */
  if (gnoll_errno) {
    return;
  }

  unsigned int tracker_idx = 0;
  for (unsigned int i = 0; i != dice->length; i++) {
    int v = dice->content[i];

    if (!contains(new_vec->content, new_vec->length, v)) {
      new_vec->content[tracker_idx] = v;
      tracker_idx++;
    }
  }
  new_vec->length = tracker_idx;
}
