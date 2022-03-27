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

int yylex(void);
int yyerror(const char* s);

int yydebug=1;

int initialize(){
    srand(time(NULL));
}

void print_vec(vec vector){
    printf("Vector Size: %d\n", vector.length);
    for(int i = 0; i != vector.length; i++){
        printf(" %d\n", vector.content[i]);
    }
}
int collapse(int * arr, int len){
    return sum(arr, len);
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

%token NUMBER SIDED_DIE FATE_DIE REPEAT PENETRATE MACRO_ACCESSOR MACRO_STORAGE
%token DIE
%token KEEP_LOWEST KEEP_HIGHEST
%token LBRACE RBRACE PLUS MINUS MULT MODULO DIVIDE_ROUND_UP DIVIDE_ROUND_DOWN

/* Defines Precedence from Lowest to Highest */
%left PLUS MINUS
%left MULT DIVIDE_ROUND_DOWN DIVIDE_ROUND_UP MODULO
%left UMINUS
%left LBRACE RBRACE
/* %left DIE SIDED_DIE FATE_DIE
%left NUMBER */




%union{
    vec values;
}
/* %type<die> DIE; */
%type<values> NUMBER;

%%
/* Rules Section */

dice: collapse{
    vec vector;
    vector = $<values>1;
    printf("%d\n", vector.content[0]);
    // YYACCEPT;
}

collapse: math{
    vec vector;
    vector = $<values>1;
    int c;
    for(int i = 0; i != vector.length; i++){
        c += vector.content[i];
    }
    vec new_vec;
    new_vec.content = malloc(sizeof(int));
    new_vec.content[0] = c;
    new_vec.length = 1;
    $<values>$ = new_vec;
}
math:
    LBRACE math RBRACE{
        $<values>$ =  $<values>2;
    }
    |
    math MULT math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;

        vector1 = $<values>1;
        vector2 = $<values>3;
        int v1 = collapse(vector1.content, vector1.length);
        int v2 = collapse(vector2.content, vector2.length);

        vec new_vec;
        new_vec.content = malloc(sizeof(int));
        new_vec.length = 1;
        new_vec.content[0] = v1 * v2;

        $<values>$ = new_vec;
    }
    |
    math DIVIDE_ROUND_UP math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;

        vector1 = $<values>1;
        vector2 = $<values>3;
        int v1 = collapse(vector1.content, vector1.length);
        int v2 = collapse(vector2.content, vector2.length);

        vec new_vec;
        new_vec.content = malloc(sizeof(int));
        new_vec.length = 1;
        new_vec.content[0] = (v1+(v2-1))/ v2;

        $<values>$ = new_vec;
    }
    |
    math DIVIDE_ROUND_DOWN math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;

        vector1 = $<values>1;
        vector2 = $<values>3;
        int v1 = collapse(vector1.content, vector1.length);
        int v2 = collapse(vector2.content, vector2.length);

        vec new_vec;
        new_vec.content = malloc(sizeof(int));
        new_vec.length = 1;
        new_vec.content[0] = v1 / v2;

        $<values>$ = new_vec;
    }
    |
    math MODULO math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;

        vector1 = $<values>1;
        vector2 = $<values>3;
        int v1 = collapse(vector1.content, vector1.length);
        int v2 = collapse(vector2.content, vector2.length);

        vec new_vec;
        new_vec.content = malloc(sizeof(int));
        new_vec.length = 1;
        new_vec.content[0] = v1 % v2;

        $<values>$ = new_vec;
    }
    |
    math PLUS math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;

        vector1 = $<values>1;
        vector2 = $<values>3;
        int v1 = collapse(vector1.content, vector1.length);
        int v2 = collapse(vector2.content, vector2.length);

        vec new_vec;
        new_vec.content = malloc(sizeof(int));
        new_vec.length = 1;
        new_vec.content[0] = v1 + v2;

        $<values>$ = new_vec;
    }
    |
    math MINUS math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;

        vector1 = $<values>1;
        vector2 = $<values>3;
        int v1 = collapse(vector1.content, vector1.length);
        int v2 = collapse(vector2.content, vector2.length);

        vec new_vec;
        new_vec.content = malloc(sizeof(int));
        new_vec.length = 1;
        new_vec.content[0] = v1 - v2;

        $<values>$ = new_vec;
    }
    |
    MINUS math %prec UMINUS{
        // Eltwise Negation
        vec vector;
        vec new_vec;

        vector = $<values>2;

        new_vec.content = malloc(sizeof(int)*vector.length);
        new_vec.length = vector.length;

        for(int i = 0; i != vector.length; i++){
            new_vec.content[i] = - vector.content[i];
        }
        $<values>$ = new_vec;
    }
    |
    drop_keep
;


drop_keep:
    die_roll KEEP_HIGHEST NUMBER
    {
        // assert $0 is len 1
        int available_amount = $<values>1.length;
        int amount_to_keep = $<values>3.content[0];

        if(available_amount > amount_to_keep){
            vec new_vector;
            new_vector.content = malloc(sizeof(int)*amount_to_keep);
            new_vector.length = amount_to_keep;

            int * arr = $<values>1.content;
            int len = $<values>1.length;

            int r = 0;
            for(int i = 0; i != amount_to_keep; i++){
                int m =  max(arr, len);
                new_vector.content[i] = m;
                pop(arr,len,m,arr);
                len -= 1;
            }

            $<values>$ = new_vector;
        }else if(available_amount < amount_to_keep){
            // Warning: More asked to keep than actually produced
            // e.g. 2d20k4
            $<values>$ = $<values>1;
        }else{
            $<values>$ = $<values>1;
        }
    }
    |
    die_roll KEEP_LOWEST NUMBER
    {
        // assert $0 is len 1
        int available_amount = $<values>1.length;
        int amount_to_keep = $<values>3.content[0];

        if(available_amount > amount_to_keep){
            vec new_vector;
            new_vector.content = malloc(sizeof(int)*amount_to_keep);
            new_vector.length = amount_to_keep;

            int * arr = $<values>1.content;
            int len = $<values>1.length;

            int r = 0;
            for(int i = 0; i != amount_to_keep; i++){
                int m =  min(arr, len);
                new_vector.content[i] = m;
                pop(arr,len,m,arr);
                len -= 1;
            }

            $<values>$ = new_vector;
        }else if(available_amount < amount_to_keep){
            // Warning: More asked to keep than actually produced
            // e.g. 2d20k4
            $<values>$ = $<values>1;
        }else{
            $<values>$ = $<values>1;
        }
    }
    |
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
        int make_negative = false;
        if (instances == 0){
            vec new_vector;
            new_vector.content = malloc(sizeof(int)*instances);
            new_vector.content[0] = 0;
            new_vector.length = 1;
            $<values>$ = new_vector;
        }
        else if (instances < 0){
            make_negative = true;
            instances = instances * -1;
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
            if (make_negative) new_vector.content[i] *= -1;
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
