#ifndef SHARED_YACC_HEADER
#define SHARED_YACC_HEADER

#include "rolls/sided_dice.h"
#include "util/vector_functions.h"

int roll_full_options(
    char* roll_request, 
    char* log_file, 
    int enable_verbosity, 
    int enable_introspection,
    int enable_mocking,
    int mocking_type,
    int mocking_seed
);

int roll(char* s);
int roll_with_breakdown(char * s, char* f);
int roll_and_write(char* s, char* f);
void roll_and_write_R(int* return_code, char** s, char** f );
int mock_roll(char* s, char* f, int mock_value, int mock_const);

#endif
