#ifndef SHARED_YACC_HEADER
#define SHARED_YACC_HEADER

#ifdef __cplusplus
extern "C"
{
#endif

#include "rolls/dice_frontend.h"
#include "util/vector_functions.h"


#define MAX_SYMBOL_LENGTH 256
#define MAX_ITERATION 20

int roll_full_options(
    char* roll_request, 
    char* log_file, 
    int enable_verbosity, 
    int enable_introspection,
    int enable_mocking,
    int enable_builtins,
    int mocking_type,
    int mocking_seed
);

int roll(char* s);
int roll_with_breakdown(char * s, char* f);
int roll_and_write(char* s, char* f);
void roll_and_write_R(int* return_code, char** s, char** f );
int mock_roll(char* s, char* f, int mock_value, int mock_const);

void load_builtins(char* root);

#ifdef __cplusplus
}
#endif

#endif
