#ifndef SHARED_YACC_HEADER
#define SHARED_YACC_HEADER

#ifdef __cplusplus
extern "C"
{
#endif

#include "rolls/dice_frontend.h"
#include "util/vector_functions.h"

#if __has_attribute(__fallthrough__)
# define fallthrough                    __attribute__((__fallthrough__))
#else
# define fallthrough                    do {} while (0)  /* fallthrough */
#endif

#define MAX_SYMBOL_LENGTH 256
#define MAX_ITERATION 20

/* Input / roll bounds: lexer rejects longer decimal tokens; core caps simulated dice. */
#define GNOLL_MAX_DECIMAL_TOKEN_LEN 64
#define GNOLL_MAX_DICE_PER_ROLL 1000000ULL

int roll_full_options(
    char* roll_request, 
    char* log_file, 
    int enable_verbosity, 
    int enable_introspection,
    int enable_mocking,
    int enable_builtins,
    int mocking_type,
    long long mocking_seed
);

int roll(char* s);
int roll_with_breakdown(char * s, char* f);
int roll_and_write(char* s, char* f);
void roll_and_write_R(int* return_code, char** s, char** f );
int mock_roll(char* s, char* f, int mock_value, long long mock_const);

void load_builtins(char* root);

/**
 * Pre-parse bounds check (decimal literal length / LLONG range, XdY dice count).
 * Sets gnoll_errno on failure; returns that code, or 0 on success.
 */
int gnoll_validate_roll_request(const char *roll_request);

/* R FFI: sets *return_code from gnoll_validate_roll_request (0 = ok). */
void gnoll_validate_roll_request_R(int* return_code, char** s);

#ifdef __cplusplus
}
#endif

#endif
