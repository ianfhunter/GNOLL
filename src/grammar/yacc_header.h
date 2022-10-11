
#ifndef __YACC_HEADER__
#define __YACC_HEADER__

#define MAX_SYMBOL_LENGTH 256
#define MAX_ITERATION 20

int initialize();
// int resolve_dice(dice die);

int sum(int * arr, unsigned int len);
int collapse(int * arr, unsigned int len);
int roll_numeric_die(int small, int big);
int roll_symbolic_die(unsigned int length_of_symbolic_array);

#endif