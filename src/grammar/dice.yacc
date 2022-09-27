/* Uncomment for better errors! (non-POSIX compliant) */
/* %define parse.error verbose */

%{

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>
#include "yacc_header.h"
#include "vector_functions.h"
#include "shared_header.h"
#include "dice_logic.h"
#include "macro_logic.h"
#include "rolls/sided_dice.h"
#include "rolls/condition_checking.h"

#define UNUSED(x) (void)(x)

int yylex(void);
int yyerror(const char* s);
void print_err_if_present(int err_code);

int yydebug=1;
int verbose = 1;
int seeded = 0;
int write_to_file = 0;
char * output_file;

// Registers

// TODO: It would be better to fit arbitrary length strings.
unsigned int MAX_SYMBOL_TEXT_LENGTH = 100;
unsigned int MAX_ITERATION = 20;

int initialize(){
    if (!seeded){
        srand(time(0));
        seeded = 1;
    }
    return 0;
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
    return random_fn(small, big);
}
int roll_symbolic_die(int length_of_symbolic_array){
    // Returns random index into symbolic array
    return roll_numeric_die(0, length_of_symbolic_array -1);
}


%}


%start gnoll_statement

%token NUMBER SIDED_DIE FATE_DIE REPEAT SIDED_DIE_ZERO
%token EXPLOSION IMPLOSION PENETRATE ONCE
%token MACRO_ACCESSOR MACRO_STORAGE SYMBOL_SEPERATOR ASSIGNMENT
%token KEEP_LOWEST KEEP_HIGHEST DROP_LOWEST DROP_HIGHEST
%token FILTER
%token LBRACE RBRACE PLUS MINUS MULT MODULO DIVIDE_ROUND_UP DIVIDE_ROUND_DOWN
%token REROLL
%token SYMBOL_LBRACE SYMBOL_RBRACE STATEMENT_SEPERATOR CAPITAL_STRING
%token DO_COUNT MAKE_UNIQUE
%token NE EQ GT LT LE GE
%token RANGE

/* Defines Precedence from Lowest to Highest */
%left STATEMENT_SEPERATOR
%left PLUS MINUS
%left MULT DIVIDE_ROUND_DOWN DIVIDE_ROUND_UP MODULO
%left KEEP_LOWEST KEEP_HIGHEST DROP_HIGHEST DROP_LOWEST
%left UMINUS
%left LBRACE RBRACE

%union{
    vec values;
}
/* %type<die> DIE; */
/* %type<values> NUMBER; */

%%
/* Rules Section */

gnoll_statement:
    gnoll_statement STATEMENT_SEPERATOR gnoll_statement
    |
    sub_statement
;
sub_statement:
    macro_statement
    |
    dice_statement
;


macro_statement:
    MACRO_STORAGE CAPITAL_STRING ASSIGNMENT math{
        // TODO: Is not recalculating if used twice.
        vec key = $<values>2;
        vec value = $<values>4;
        register_macro(key.symbols[0], &value);
    }
;
dice_statement: 
    die_statement REPEAT dice_statement{
        vec vector1;
        vec vector2;

        vector1 = $<values>1;
        vector2 = $<values>2;

        vec new_vec;
        new_vec.length = vector1.length+vector2.length ;
        new_vec.dtype = vector1.dtype;
  
        // TODO: assert types are the same?
        if (new_vec.dtype == SYMBOLIC){
            new_vec.symbols = calloc(sizeof(char **), new_vec.length);
            concat_symbols(
                 vector1.symbols, vector1.length,
                 vector2.symbols, vector2.length,
                 new_vec.symbols
            );
        }else{
            new_vec.content = calloc(sizeof(int), new_vec.length);
            concat_numbers(
                 vector1.content, vector1.length,
                 vector2.content, vector2.length,
                 new_vec.content
            );
        }

        $<values>$ = new_vec;
    }
    |
    die_statement
;

die_statement: math{

    vec vector;
    vec new_vec;
    vector = $<values>1;

    new_vec = vector;
    //  Step 1: Collapse pool to a single value if nessicary
    collapse_vector(&vector, &new_vec);

    // Step 2: Output
    FILE *fp;

    if(write_to_file){
        fp = fopen(output_file, "a+");
    }

    for(int i = 0; i!= new_vec.length;i++){
        if (new_vec.dtype == SYMBOLIC){
            // TODO: Strings >1 character
            if (verbose){
                printf("%s;", new_vec.symbols[i]);
            }
            if(write_to_file){
                fprintf(fp, "%s;", new_vec.symbols[i]);
            }
        }else{
            if(verbose){
                printf("%d;", new_vec.content[i]);
            }
            if(write_to_file){
                fprintf(fp, "%d;", new_vec.content[i]);
            }
        }
    }
    if(verbose){
        printf("\n");
    }

    if(write_to_file){
        fclose(fp);
    }
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

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Division unsupported for symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 * v2;
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
    }
    |
    math DIVIDE_ROUND_UP math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;
        vector1 = $<values>1;
        vector2 = $<values>3;

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Division unsupported for symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = (v1+(v2-1))/ v2;
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
    }
    |
    math DIVIDE_ROUND_DOWN math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;
        vector1 = $<values>1;
        vector2 = $<values>3;

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Modulo unsupported for symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 / v2;
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
    }
    |
    math MODULO math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;

        vector1 = $<values>1;
        vector2 = $<values>3;

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Modulo unsupported for symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 % v2;
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
    }
    |
    math PLUS math{
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;
        vector1 = $<values>1;
        vector2 = $<values>3;

        if (
            (vector1.dtype == SYMBOLIC && vector2.dtype == NUMERIC) ||
            (vector2.dtype == SYMBOLIC && vector1.dtype == NUMERIC)
        ){
            printf("Addition not supported with mixed dice types.");
            YYABORT;
            yyclearin;
        } else if (vector1.dtype == SYMBOLIC){
            vec new_vec;
            unsigned int concat_length = vector1.length + vector2.length;
            new_vec.symbols = calloc(sizeof(char *), concat_length);
            for (int i = 0; i != concat_length; i++){
                new_vec.symbols[i] = calloc(sizeof(char), MAX_SYMBOL_TEXT_LENGTH);
            }
            new_vec.length = concat_length;
            new_vec.dtype = vector1.dtype;

            concat_symbols(
                vector1.symbols, vector1.length,
                vector2.symbols, vector2.length,
                new_vec.symbols
            );
            // free(vector1.symbols);
            // free(vector2.symbols);

            $<values>$ = new_vec;

        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.dtype = vector1.dtype;
            new_vec.content[0] = v1 + v2;

            $<values>$ = new_vec;
        }

    }
    |
    math MINUS math{
        vec vector1;
        vec vector2;
        vector1 = $<values>1;
        vector2 = $<values>3;
        if (
            (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC)
        ){
            // It's not clear whether {+,-} - {-, 0} should be {+} or {+, 0}!
            // Therfore, we'll exclude it.
            printf("Subtract not supported with symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            // Collapse both sides and subtract

            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 - v2;
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }

    }
    |
    MINUS math %prec UMINUS{
        // Eltwise Negation
        vec vector;
        vector = $<values>2;

        if (vector.dtype == SYMBOLIC){
            printf("Symbolic Dice, Cannot negate. Consider using Numeric dice or post-processing.");
            YYABORT;
            yyclearin;
        } else {
            vec new_vec;

            new_vec.content = calloc(sizeof(int), vector.length);
            new_vec.length = vector.length;
            new_vec.dtype = vector.dtype;

            for(int i = 0; i != vector.length; i++){
                new_vec.content[i] = - vector.content[i];
            }
            $<values>$ = new_vec;

        }
    }
    |
    collapsing_dice_operations
;

collapsing_dice_operations:
    dice_operations DO_COUNT{

        vec new_vec;
        vec dice = $<values>1;
        initialize_vector(&new_vec, NUMERIC, 1);

        new_vec.content[0] = dice.length;
        $<values>$ = new_vec;
    }
    |
    dice_operations{

        vec vector;
        vector = $<values>1;

        if (vector.dtype == SYMBOLIC){
            // Symbolic, Impossible to collapse
            $<values>$ = vector;
        }
        else{
            // Collapse if Nessicary
            if(vector.length > 1){
                int result = sum(vector.content, vector.length);

                vec new_vector;
                initialize_vector(&new_vector, NUMERIC, 1);
                new_vector.content[0] = sum(vector.content, vector.length);

                $<values>$ = new_vector;
            }else{
                $<values>$ = vector;
            }

        }
    }
;


dice_operations:

    die_roll REROLL REROLL condition NUMBER{

        vec dice = $<values>1;
        int check = $<values>4.content[0];

        if(dice.dtype == NUMERIC){
            int count = 0;
            while (! check_condition(&dice, &$<values>5, check)){
                if (count > MAX_ITERATION){
                    printf("MAX ITERATION LIMIT EXCEEDED: REROLL");
                    break;
                }
                vec number_of_dice;
                initialize_vector(&number_of_dice, NUMERIC, 1);
                number_of_dice.content[0] = dice.source.number_of_dice;

                vec die_sides;
                initialize_vector(&die_sides, NUMERIC, 1);
                die_sides.content[0] = dice.source.die_sides;

                roll_plain_sided_dice(
                    &number_of_dice,
                    &die_sides,
                    &dice,
                    dice.source.explode,
                    1
                );
                count ++;
            }
            $<values>$ = dice;
        }else{
            printf("No support for Symbolic die rerolling yet!");
        }
    }
    |die_roll REROLL condition NUMBER{

        vec dice = $<values>1;
        int check = $<values>3.content[0];

        if(dice.dtype == NUMERIC){
            if (check_condition(&dice, &$<values>4, check)){

                vec number_of_dice;
                initialize_vector(&number_of_dice, NUMERIC, 1);
                number_of_dice.content[0] = dice.source.number_of_dice;

                vec die_sides;
                initialize_vector(&die_sides, NUMERIC, 1);
                die_sides.content[0] = dice.source.die_sides;

                roll_plain_sided_dice(
                    &number_of_dice,
                    &die_sides,
                    &$<values>$,
                    dice.source.explode,
                    1
                );
            }else{
                // No need to reroll
                $<values>$ = $<values>1;
            }
        }else{
            printf("No support for Symbolic die rerolling yet!");
        }
    }
    |
    dice_operations FILTER condition NUMBER{
        vec new_vec;
        vec dice = $<values>1;
        vec condition = $<values>4;
        int check = $<values>3.content[0];

        if(dice.dtype == NUMERIC){
            initialize_vector(&new_vec, NUMERIC, dice.length);
            filter(&dice, &condition, check, &new_vec);

            $<values>$ = new_vec;
        }else{
            printf("No support for Symbolic die rerolling yet!");
        }

    }
    |
    dice_operations MAKE_UNIQUE{
        // TODO
        vec new_vec;
        vec cond_vec;
        vec dice = $<values>1;

        if(dice.dtype == NUMERIC){
            initialize_vector(&new_vec, NUMERIC, dice.length);
            filter_unique(&dice, &new_vec);

            $<values>$ = new_vec;
        }else{
            printf("No support for Symbolic die rerolling yet!");
        }
    }
    |
    dice_operations KEEP_HIGHEST NUMBER
    {
        vec keep_vector = $<values>3;
        vec new_vec;
        unsigned int num_to_hold = keep_vector.content[0];

        unsigned int err = keep_highest_values(&$<values>1, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighestN.");
            YYABORT;
            yyclearin;
        }
        $<values>$ = new_vec;
    }
    |
    dice_operations DROP_HIGHEST NUMBER
    {
        vec keep_vector = $<values>3;
        vec new_vec;
        unsigned int num_to_hold = keep_vector.content[0];

        unsigned int err = drop_highest_values(&$<values>1, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighestN.");
            YYABORT;
            yyclearin;
        }
        $<values>$ = new_vec;
    }
    |
    dice_operations KEEP_LOWEST NUMBER
    {
        vec roll_vector;
        vec keep_vector;
        unsigned int num_to_hold;
        keep_vector = $<values>3;
        num_to_hold = keep_vector.content[0];

        vec new_vec;
        unsigned int err = keep_lowest_values(&$<values>1, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepLowestN.");
            YYABORT;
            yyclearin;
        }
        $<values>$ = new_vec;
    }
    |
    dice_operations DROP_LOWEST NUMBER
    {
        vec roll_vector;
        vec keep_vector;
        unsigned int num_to_hold;
        keep_vector = $<values>3;
        num_to_hold = keep_vector.content[0];

        vec new_vec;
        unsigned int err = drop_lowest_values(&$<values>1, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepLowestN.");
            YYABORT;
            yyclearin;
        }
        $<values>$ = new_vec;
    }
    |
    dice_operations KEEP_HIGHEST
    {
        unsigned int num_to_hold = 1;
        vec new_vec;
        unsigned int err = keep_highest_values(&$<values>1, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighest1.");
            YYABORT;
            yyclearin;
        }
        $<values>$ = new_vec;
    }
    |
    dice_operations DROP_HIGHEST
    {
        vec roll_vec = $<values>1;
        unsigned int num_to_hold = 1;

        vec new_vec;
        unsigned int err = drop_highest_values(&roll_vec, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighest1.");
            YYABORT;
            yyclearin;
        }
        $<values>$ = new_vec;
    }
    |
    dice_operations KEEP_LOWEST
    {
        unsigned int num_to_hold = 1;

        vec new_vec;
        unsigned int err = keep_lowest_values(&$<values>1, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighest1.");
            YYABORT;
            yyclearin;
        }
        $<values>$ = new_vec;
    }
    |
    dice_operations DROP_LOWEST
    {
        vec roll_vec = $<values>1;
        unsigned int num_to_hold = 1;

        vec new_vec;
        unsigned int err = drop_lowest_values(&roll_vec, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighest1.");
            YYABORT;
            yyclearin;
        }
        $<values>$ = new_vec;
    }
    |
    die_roll
    {
    }
;

die_roll:
   NUMBER die_symbol NUMBER EXPLOSION ONCE
    {
        int start_from = $<values>2.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &$<values>1,
            &$<values>3,
            &$<values>$,
            ONLY_ONCE_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
    |
    die_symbol NUMBER EXPLOSION ONCE
    {

        int start_from = $<values>1.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &number_of_dice,
            &$<values>2,
            &$<values>$,
            ONLY_ONCE_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
    |
   NUMBER die_symbol NUMBER EXPLOSION PENETRATE
    {

        int start_from = $<values>2.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &$<values>1,
            &$<values>3,
            &$<values>$,
            PENETRATING_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
    |
    die_symbol NUMBER EXPLOSION PENETRATE
    {
        int start_from = $<values>1.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &number_of_dice,
            &$<values>2,
            &$<values>$,
            PENETRATING_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
    |
   NUMBER die_symbol NUMBER EXPLOSION
    {

        int start_from = $<values>2.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &$<values>1,
            &$<values>3,
            &$<values>$,
            PENETRATING_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
    |
    die_symbol NUMBER EXPLOSION
    {

        int start_from = $<values>1.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &number_of_dice,
            &$<values>2,
            &$<values>$,
            STANDARD_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
    |
    NUMBER die_symbol NUMBER
    {
        int start_from = $<values>2.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &$<values>1,
            &$<values>3,
            &$<values>$,
            NO_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
    |
    die_symbol NUMBER
    {

        int start_from = $<values>1.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &number_of_dice,
            &$<values>2,
            &$<values>$,
            NO_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
    |
    NUMBER die_symbol MODULO
    {
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 100;

        int err = roll_plain_sided_dice(
            &$<values>1,
            &dice_sides,
            &$<values>$,
            NO_EXPLOSION,
            1
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
    |
    die_symbol MODULO
    {

        vec num_dice;
        initialize_vector(&num_dice, NUMERIC, 1);
        num_dice.content[0] = 1;
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 100;

        int err = roll_plain_sided_dice(
            &num_dice,
            &dice_sides,
            &$<values>$,
            NO_EXPLOSION,
            1
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
    |
    NUMBER die_symbol DO_COUNT
    {

        int start_from = $<values>2.content[0];

        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 2;

        int err = roll_plain_sided_dice(
            &$<values>1,
            &dice_sides,
            &$<values>$,
            NO_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
    |
    die_symbol DO_COUNT
    {
        int start_from = $<values>1.content[0];

        vec num_dice;
        initialize_vector(&num_dice, NUMERIC, 1);
        num_dice.content[0] = 1;
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 2;

        int err = roll_plain_sided_dice(
            &num_dice,
            &dice_sides,
            &$<values>$,
            NO_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
    |
    NUMBER FATE_DIE
    {
        vec result_vec;
        initialize_vector(&result_vec, SYMBOLIC, $<values>1.content[0]);

        int err = roll_symbolic_dice(
            &$<values>1,
            &$<values>2,
            &result_vec
        );
        $<values>$ = result_vec;
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
    |
    FATE_DIE
    {
        vec result_vec;
        vec number_of_dice;
        initialize_vector(&result_vec, SYMBOLIC, 1);
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_symbolic_dice(
            &number_of_dice,
            &$<values>1,
            &result_vec
        );
        $<values>$ = result_vec;

        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
    |
    custom_symbol_dice
    |
    NUMBER
    ;

custom_symbol_dice:
    NUMBER die_symbol SYMBOL_LBRACE csd SYMBOL_RBRACE
    {

        // TODO: Multiple ranges

        vec result_vec;
        initialize_vector(&result_vec, SYMBOLIC, $<values>1.content[0]);

        int err = roll_symbolic_dice(
            &$<values>1,
            &$<values>4,
            &result_vec
        );
        $<values>$ = result_vec;
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
    |
    die_symbol SYMBOL_LBRACE csd SYMBOL_RBRACE
    {
        vec csd = $<values>3;
        vec result_vec;
        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = 0;

        if (csd.dtype == NUMERIC){
            vec dice_sides;
            vec num_dice;
            initialize_vector(&dice_sides, NUMERIC, 1);
            initialize_vector(&num_dice, NUMERIC, 1);
            initialize_vector(&result_vec, NUMERIC, 1);
            num_dice.content[0] = 1;

            int start_value = csd.content[0];
            int end_value = csd.content[csd.length-1];
            dice_sides.content[0] = end_value - start_value + 1;

            // Range
            err = roll_plain_sided_dice(
                &num_dice,
                &dice_sides,
                &result_vec,
                NO_EXPLOSION,
                start_value
            );

        }else{
            initialize_vector(&result_vec, SYMBOLIC, 1);
            // Custom Symbol
            err = roll_symbolic_dice(
                &number_of_dice,
                &$<values>3,
                &result_vec
            );
        }
        $<values>$ = result_vec;
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
    |
    MACRO_ACCESSOR CAPITAL_STRING{
        vec vector;
        vector = $<values>2;
        char * name = vector.symbols[0];

        vec new_vector;
        search_macros(name, &new_vector);

        // TODO: Apply rerolls!

        $<values>$ = new_vector;
    }
    ;
csd:
    CAPITAL_STRING SYMBOL_SEPERATOR csd{
        vec l;
        vec r;
        l = $<values>1;
        r = $<values>3;

        vec new_vector;
        initialize_vector(&new_vector, SYMBOLIC, l.length + r.length);

        concat_symbols(
            l.symbols, l.length,
            r.symbols, r.length,
            new_vector.symbols
        );
        $<values>$ = new_vector;

    }
    |
    NUMBER RANGE NUMBER{
        vec start = $<values>1;
        vec end = $<values>3;

        int s = start.content[0];
        int e = end.content[0];


        if (s > e){
            printf("Range: %i -> %i\n", s, e);
            printf("Reversed Ranged not supported yet.");
            YYABORT;
            yyclearin;
        }

        int spread = e - s + 1; // 2-2= 1 2-3=2, etc

        vec new_vector;
        initialize_vector(&new_vector, NUMERIC, spread);
        for (int i = 0; i <= (e-s); i++){
            new_vector.content[i] = s+i;
        }
        $<values>$ = new_vector;
    }
    |
    CAPITAL_STRING
    ;

condition: EQ | LT | GT | LE | GE | NE ;

die_symbol:
    SIDED_DIE{
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        new_vec.content[0] = 1;
        $<values>$ = new_vec;
    }
    |
    SIDED_DIE_ZERO{
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        new_vec.content[0] = 0;
        $<values>$ = new_vec;
    }
;


%%
/* Subroutines */

typedef struct yy_buffer_state * YY_BUFFER_STATE;
extern int yyparse();
extern YY_BUFFER_STATE yy_scan_string(char * str);
extern void yy_delete_buffer(YY_BUFFER_STATE buffer);

int roll(char * s){
    initialize();
    verbose = 0;
    YY_BUFFER_STATE buffer = yy_scan_string(s);
    yyparse();

    yy_delete_buffer(buffer);
    return 0;
}
int roll_verbose(char * s){
    initialize();
    verbose = 1;
    YY_BUFFER_STATE buffer = yy_scan_string(s);

    yyparse();

    yy_delete_buffer(buffer);
    return 0;
}
int roll_and_write(char * s, char * f){
    /* Write the result to file. */
    write_to_file = 1;
    output_file = f;
    if(verbose) printf("Rolling: %s\n", s);
    return roll(s);
}
int mock_roll(char * s, char * f, int mock_value, int quiet, int mock_const){
    init_mocking(mock_value, mock_const);
    verbose = !quiet;
    return roll_and_write(s, f);
}

char * concat_strings(char ** s, int num_s){
    int size_total = 0;
    int spaces = 0;
    for(int i = 1; i != num_s + 1; i++){
        size_total += strlen(s[i]) + 1;
    }
    if (num_s > 1){
        spaces = 1;
        size_total -= 1;  // no need for trailing space
    }
    char * result;
    result = (char *)calloc(sizeof(char), (size_total+1));

    for(int i = 1; i != num_s + 1; i++){
        strcat(result, s[i]);
        if (spaces && i < num_s){
            strcat(result, " ");    // Add spaces
        }
    }

    return result;

}

int main(int argc, char **str){
    char * s = concat_strings(str, argc - 1);
    return roll_verbose(s);
}

int yyerror(s)
const char *s;
{
    fprintf(stderr, "%s\n", s);

    if(write_to_file){
        FILE *fp;
        fp = fopen(output_file, "a+");
        fprintf(fp, "%s;", s);
        fclose(fp);
    }
    return(1);

}

int yywrap(){
    return (1);
}
void print_err_if_present(int err_code){
    switch(err_code){
        case 1:{
            printf("Negative Dice Sides not Allowed\n");
            break;
        }
    }
}
