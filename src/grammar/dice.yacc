%code requires{
    #include "shared_header.h"
}
%error-verbose
%{

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <stdbool.h>
#include "yacc_header.h"
#include "shared_header.h"

int regs[26];

int base;

int initialize(){
    srand(time(NULL));
}

void print_vec(vec vector){
    printf("Vector Size: %d\n", vector.length);
    for(int i = 0; i != vector.length; i++){
        printf(" %d\n", vector.content[i]);
    }
}

int sum(int * arr, int len){
    int result = 0;
    for(int i = 0; i != len; i++) result += arr[i];
    return result;
}

int roll_numeric_die(int small, int big){
    // Returns random value between small and big
    return rand()%(big+1-small)+small;
}
int roll_symbolic_die(int length_of_symbolic_array){
    // Returns random index into symbolic array
    return rand()%(length_of_symbolic_array);
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
void pop(int * arr, int len, int value, int * new_arr){
    // This could be done in-place.
    bool seen = false;
    for(int i = 0; i != len; i++){
        if (arr[i] == value && !seen){
            seen = true;
        }
        else if(seen){
            new_arr[i] = arr[i + 1];
        }else{
            new_arr[i] = arr[i];
        }
    }
}



%}


%start dice

%token NUMBER SIDED_DIE FATE_DIE PLUS MINUS MULT MODULO DIVIDE_ROUND_UP DIVIDE_ROUND_DOWN REPEAT PENETRATE MACRO_ACCESSOR MACRO_STORAGE
%token DIE
%token KEEP_LOWEST KEEP_HIGHEST

/* Defines Precedence from Lowest to Highest */
/* %left '+' '-'
%left '*' '/' '%' */
/* %left UMINUS */


%union{
    vec values;
    // int * values;
    // struct dice * die;

}
/* %type<die> DIE; */
%type<values> NUMBER;

%%
/* Rules Section */

dice: drop_keep{
    vec vector;
    vector = $<values>1;
    printf("%d\n", vector.content[0]);
}

// A Die Roll Can be:
// - [x]d[y]kh
// - [x]d[y]kl
// - [x]d[y]kh[z]
// - [x]d[y]kl[z]
// - [x]d[y]
// - (1)d[x]
// - [x]dF
// - (1)dF
// - [x]
    /* NUMBER DIE KEEP_LOWEST {
        // Original Array
        int len = $<int>1;
        int result[len];

        // Dropped Array
        int len2 = len -1;
        int result2[len2];

        // Get all values
        for(int i = 0; i != len; i++){
            result[i] = resolve_dice($2);
            printf("Recorded Value: %d\n", result[i]);
        }
        // Get Minimum Values
        int val = 0;
        val += min(result, len);
        printf("Minimum Value: %d\n", val);
        pop(result, len, val, result2);

        int total = 0;
        for(int i = 0; i != len2; i++){
            total += result2[i];
            printf("Running Total: %d\n", total);
        }

        $<int>$ = total;
    }
    |
    NUMBER DIE
    {
        int result = 0;
        for(int i = 0; i != $<int>1; i++){
            result += resolve_dice($2);
        }
        $<int>$ = result;
    }
    | */
drop_keep:
    die_roll KEEP_HIGHEST
    {
        if($<values>1.length > 1){
            // print_vec($<values>1);
            int result = max($<values>1.content, $<values>1.length);
            vec vector;
            vector.content = malloc(sizeof(int));
            vector.content[0] = result;
            vector.length = 1;
            $<values>$ = vector;
        }else{
            $<values>$ = $<values>1;
        }
    }
    |
    die_roll KEEP_LOWEST
    {
        if($<values>1.length > 1){
            // print_vec($<values>1);
            int result = min($<values>1.content, $<values>1.length);
            vec vector;
            vector.content = malloc(sizeof(int));
            vector.content[0] = result;
            vector.length = 1;
            $<values>$ = vector;
        }else{
            $<values>$ = $<values>1;
        }
    }
    |
    die_roll
    {
        if($<values>1.length > 1){
            int result = sum($<values>1.content, $<values>1.length);
            vec vector;
            vector.content = malloc(sizeof(int));
            vector.content[0] = result;
            vector.length = 1;
            $<values>$ = vector;
        }else{
            $<values>$ = $<values>1;
        }
    }
die_roll:
    NUMBER SIDED_DIE NUMBER
    {
        // e.g. 2d20

        vec num_dice;
        num_dice = $<values>1;
        int instances = num_dice.content[0];
        if (instances < 0){
            printf("Cannot roll a negative amount of dice");
            YYABORT;
            yyclearin;
        }


        vec vector;
        vector = $<values>3;
        int max = vector.content[0];
        if (max <= 0){
            printf("Cannot roll a zero or negative number");
            YYABORT;
            yyclearin;
        }


        vec new_vector;
        new_vector.content = malloc(sizeof(int)*instances);
        new_vector.length = instances;

        int result = 0;
        for (int i = 0; i!= instances; i++){
            new_vector.content[i] += roll_numeric_die(1, max);
        }

        $<values>$ = new_vector;
    }
    |
    SIDED_DIE NUMBER
    {
        // e.g. d4, it is implied that it is a single dice
        vec vector;
        vector = $<values>2;
        int max = vector.content[0];
        if (max <= 0){
            printf("Cannot roll a zero or negative number");
            YYABORT;
            yyclearin;
        }


        int result = roll_numeric_die(1, max);

        vec new_vector;
        new_vector.content = malloc(sizeof(int));
        new_vector.content[0] = result;
        new_vector.length = 1;

        $<values>$ = new_vector;
    }
    |
    NUMBER
    ;



/* die_result:
    SIDED_DIE NUMBER
    {
        struct numericalDice die;
        die.minValue = 1;
        die.maxValue = 2;
        $<die>$ = die;
        // return die;
    }
    |
    FATE_DIE
    {
        struct symbolicDice die;
        die.symbols = malloc(sizeof(char)*2);
        die.symbols[0] = '-';
        die.symbols[1] = '+';
        die.num_symbols = 2;
        // $$.die = die;
        $<die>$ = die;
        // return dice;
    }
    ; */

/* Macros */
/*
list:
     |
    list stat '\n'
     |
    list error '\n'
    {
        yyerrok;
    }
    ;

stat:    expr
    {
      printf("%d\n", $1);
    }
    ;

expr:    '(' expr ')'
    {
      $$ = $2;
    }
    |
    expr '*' expr
    {
        $$ = $1 * $3;
    }
    |
    expr '/' expr
    {
        $$ = $1 / $3;
    }
    |
    expr '%' expr
    {
        $$ = $1 % $3;
    }
    |
    expr '+' expr
    {
        $$ = $1 + $3;
    }
    |
    expr '-' expr
    {
        $$ = $1 - $3;
    }
    |
    expr '&' expr
    {
        $$ = $1 & $3
    }
    |
    expr '|' expr
    {
        $$ = $1 | $3
    }
    |
    '-' expr %prec UMINUS
    {
        $$ = -$2;
    }
    |
    NUMBER
    ;
*/


%%

int main(){
    initialize();
    return(yyparse());
}

int yyerror(s)
char *s;
{
    fprintf(stderr, "%s\n", s);
    return(1);
}

int yywrap(){
    return (1);
}
