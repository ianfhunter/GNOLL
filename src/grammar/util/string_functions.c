
#include "util/string_functions.h"
#include <string.h>
#include "util/safe_functions.h"

extern int gnoll_errno;

char * concat_strings(char ** s, unsigned long long num_s){
  /**
   * @brief Given an array of strings, join them together.
   * @param s array of strings
   * @param num_s length of above array
   * @return a string containing both substrings
   */
    if (num_s == 1){
        return s[0];
    }
    unsigned long long size_total = 0;
    unsigned long long spaces = 0;
    for(unsigned long long i = 1; i != num_s + 1; i++){
        size_total += strlen(s[i]) + 1;
    }
    if (num_s > 1){
        spaces = 1;
        size_total -= 1;  // no need for trailing space
    }
    
    // printf("Size Total %lu\n", size_total);
    
    char * result = (char *)safe_calloc((size_total+1), sizeof(char));
    if(gnoll_errno){return NULL;}

    for(unsigned long long i = 1; i != num_s + 1; i++){
        // printf()
        strcat(result, s[i]);
        if (spaces && i < num_s){
            strcat(result, " ");    // Add spaces
        }
    }
    return result;
}
