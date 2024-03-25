#include "util/vector_functions.h"

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "operations/conditionals.h"
#include "shared_header.h"
#include "util/safe_functions.h"
#include "shared_header.h"

extern int gnoll_errno;

void light_initialize_vector(vec *vector, DIE_TYPE dt,
                             unsigned long long number_of_items) {
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
    vector->storage.content = (long long*)safe_calloc(number_of_items, sizeof(long long));
    if (gnoll_errno) return;
  } else if (dt == SYMBOLIC) {
    vector->storage.symbols = (char**)safe_calloc(1, sizeof(char **));
  }
}


void initialize_vector_pointer(vec ***vector, DIE_TYPE dt, unsigned long long number_of_items) {
  // Initialize a pointer to a vector
  // Note: Is not a 2d vector. 
    *vector = (vec**)safe_calloc(1, sizeof(vec*));
    if (gnoll_errno) {
        return;
    }
    (*vector)[0] = (vec*)safe_malloc(sizeof(vec));
    initialize_vector((*vector)[0], dt, number_of_items); 
}

void initialize_vector(vec *vector, DIE_TYPE dt, unsigned long long number_of_items) {

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
    vector->storage.content = (long long*)safe_calloc(number_of_items, sizeof(long long));
    if (gnoll_errno) return;
  } 
  else if (dt == SYMBOLIC) 
  {
    vector->storage.symbols = (char**)safe_calloc(number_of_items, sizeof(char *));
    if (gnoll_errno) return;

    for (unsigned long long i = 0; i < number_of_items; i++) {
      vector->storage.symbols[i] = (char*)safe_calloc(MAX_SYMBOL_LENGTH, sizeof(char));
      if (gnoll_errno) return;
    }
  }
}

void concat_symbols(char **arr1, unsigned long long len1, char **arr2,
                    unsigned long long len2, char **new_arr) {
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

  for (unsigned long long i = 0; i != len1; i++) {
    strcpy(new_arr[i], arr1[i]);
    // free(arr1[i]);
  }
  for (unsigned long long i = 0; i != len2; i++) {
    unsigned long long idx = len1 + i;
    strcpy(new_arr[idx], arr2[i]);
    // free(arr2[i]);
  }
}

void pop(long long *arr, unsigned long long len, long long value, long long *new_arr) {
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
  bool seen = false;

  for (unsigned long long i = 0; i != len; i++) {
    if (arr[i] == value && !seen) {
      seen = true;
      // Don't insert into new area.
    } else if (seen) {
      new_arr[i - 1] = arr[i];
    } else {
      new_arr[i] = arr[i];
    }
  }
}

bool contains(long long *arr, unsigned long long len, long long value) {
  /**
   * @brief Checks if a value exists in an array
   * @param arr
   * @param len
   * @param value
   * @return true or false (1 or 0)
   */
  if (gnoll_errno) {
    return true;
  }

  for (unsigned long long i = 0; i != len; i++) {
    if (arr[i] == value) return true;
  }
  return false;
}

long long min_in_vec(long long *arr, unsigned long long len) {
  /**
   * @brief Return the smallest value from an array
   * @param arr
   * @param len
   * @return minimum value
   */
  if (gnoll_errno) {
    return 0;
  }

  long long lowest = LLONG_MAX;
  for (unsigned long long i = 0; i != len; i++) {
    if (arr[i] < lowest) lowest = arr[i];
  }
  return lowest;
}

long long max_in_vec(long long *arr, unsigned long long len) {
  /**
   * @brief Return the biggest value in an array
   * @param arr
   * @param len
   * @return maximum value
   */
  if (gnoll_errno) {
    return 0;
  }

  long long highest = LLONG_MIN;
  for (unsigned long long i = 0; i != len; i++) {
    if (arr[i] > highest) highest = arr[i];
  }
  return highest;
}
void abs_vec(vec *x) {
  for (unsigned long long i = 0; i != x->length; i++) {
    long long v = x->storage.content[i];
    if (v < 0) {
      x->storage.content[i] *= -1;
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

  printf("Vector Size: %llu\n", vector.length);
  if (vector.dtype == NUMERIC) {
    printf("Vector Type: NUMERIC\n");
    for (unsigned long long i = 0; i != vector.length; i++) {
      printf("\t%lld\n", vector.storage.content[i]);
    }
  } else {
    printf("Vector Type: SYMBOLIC\n");
    printf("Symbols:\n");
    for (unsigned long long i = 0; i != vector.length; i++) {
      printf("\t- %s\n", vector.storage.symbols[i]);
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
       &new_vector->storage.symbols,
       vector->storage.symbols,
       vector->length,
       MAX_SYMBOL_LENGTH
    );
    
    new_vector->length = vector->length;
    new_vector->dtype = SYMBOLIC;
    new_vector->has_source = false;
  } 
  else {
    long long c = 0;
    for (unsigned long long i = 0; i != vector->length; i++) {
      c += vector->storage.content[i];
    }

    new_vector->storage.content = (long long*)safe_calloc(sizeof(long long), 1);
    if (gnoll_errno) return;
    new_vector->storage.content[0] = c;
    new_vector->length = 1;
    new_vector->dtype = NUMERIC;
    new_vector->has_source = false;
  }
  return;
}


void keep_logic(vec *vector, vec **output_vector, unsigned long long number_to_keep,
                bool keep_high) {

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

  unsigned long long available_amount = vector->length;

  if (vector->dtype == SYMBOLIC) {
    printf(
        "Symbolic Dice, Cannot determine value. Consider using filters "
        "instead");
    gnoll_errno = UNDEFINED_BEHAVIOUR;
    return;
  }
  
  if (available_amount > number_to_keep) {

    // output_vector->content = (int*)safe_calloc(sizeof(int), number_to_keep);
    // if (gnoll_errno) {
    //   return;
    // }
    // output_vector->length = number_to_keep;

    long long *arr = vector->storage.content;
    long long *new_arr;
    unsigned long long length = vector->length;

    // while (number needed)
    //     Get Max/Min from vector
    //     Store in output
    for (unsigned long long i = 0; i != number_to_keep; i++) {
      long long m;
      if (keep_high) {
        m = max_in_vec(arr, length);
      } else {
        m = min_in_vec(arr, length);
      }

      (*output_vector)->storage.content[i] = m;
      new_arr = (long long*)safe_calloc(sizeof(long long), length - 1);

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
    (*output_vector)->dtype = vector->dtype;
  } else {
    // e.g. 2d20k4 / 2d20kh2
    printf("Warning: KeepHighest: Keeping <= produced amount");
    *output_vector = vector;
  }
}


void keep_lowest_values(vec *vector, vec **new_vector,
                        unsigned long long number_to_keep) {
  /**
   * @brief Keep the lowest values from a set of dice
   */
  keep_logic(vector, new_vector, number_to_keep, false);
}

void keep_highest_values(vec *vector, vec **new_vector,
                         unsigned long long number_to_keep) {

  /**
   * @brief Keep the Highest values from a set of dice
   */
  keep_logic(vector, new_vector, number_to_keep, true);
}

void drop_lowest_values(vec *vector, vec **new_vector,
                        unsigned long long number_to_drop) {
  /**
   * @brief Drop the lowest values from a set of dice
   */
  long long calc_keep = (long long)vector->length - (long long)number_to_drop;
  unsigned long long number_to_keep;

  if (calc_keep > 0) {
    number_to_keep = (unsigned long long)calc_keep;
  } else {
    number_to_keep = (unsigned long long)vector->length;
  }
  keep_logic(vector, new_vector, number_to_keep, true);
}

void drop_highest_values(vec *vector, vec **new_vector,
                         unsigned long long number_to_drop) {
  /**
   * @brief Drop the highest values from a set of dice
   */

  long long calc_keep = (long long)vector->length - (long long)number_to_drop;
  unsigned long long number_to_keep;

  if (calc_keep > 0) {
    number_to_keep = (unsigned long long)calc_keep;
  } else {
    number_to_keep = (unsigned long long)vector->length;
  }
  keep_logic(vector, new_vector, number_to_keep, 0);
}

void extract_symbols(char **symbols_list, char **result_symbols, long long *indexes,
                     unsigned long long idx_length) {
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
  for (unsigned long long i = 0; i != idx_length; i++) {
    if (result_symbols[i]) {
      free(result_symbols[i]);
    }
  }

  for (unsigned long long i = 0; i != idx_length; i++) {
    long long index = indexes[i];
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

  unsigned long long success_idx = 0;
  for (unsigned long long i = 0; i != dice->length; i++) {
    long long v = dice->storage.content[i];
    if (comp_op == IF_EVEN || comp_op == IF_ODD){
      if(check_condition_scalar(v, v, (COMPARATOR)comp_op)){
        output->storage.content[success_idx] = v;
        success_idx++;
      }
    }else{

      long long compare_to = cond->storage.content[0];

      if (check_condition_scalar(v, compare_to, (COMPARATOR)comp_op)) {
        output->storage.content[success_idx] = v;
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

  unsigned long long tracker_idx = 0;
  for (unsigned long long i = 0; i != dice->length; i++) {
    long long v = dice->storage.content[i];

    if (!contains(new_vec->storage.content, new_vec->length, v)) {
      new_vec->storage.content[tracker_idx] = v;
      tracker_idx++;
    }
  }
  new_vec->length = tracker_idx;
}
