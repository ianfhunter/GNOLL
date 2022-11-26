/* Uncomment for better errors! (non-POSIX compliant) */
/* %define parse.error verbose */

%{

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>
#include <assert.h>
#include <errno.h>
#include "shared_header.h"
#include "external/pcg_basic.h"
#include "external/tinydir.h"
#include "operations/macros.h"
#include "operations/conditionals.h"
#include "rolls/dice_core.h"
#include "rolls/dice_frontend.h"
#include "util/mocking.h"
#include "util/safe_functions.h"
#include "util/array_functions.h"
#include "util/vector_functions.h"
#include "util/string_functions.h"

#define UNUSED(x) (void)(x)
// Avoid conflicts with MacOs predefined macros
#define MAXV(x, y) (((x) > (y)) ? (x) : (y))
#define MINV(x, y) (((x) < (y)) ? (x) : (y))
#define ABSV(x) (((x) < 0) ? (-x) : (x))

int yylex(void);
int yyerror(const char* s);
int yywrap();

//TODO: move to external file 

#ifdef JUST_YACC
int yydebug=1;
#endif

int verbose = 0;
int dice_breakdown = 0;
int seeded = 0;
int write_to_file = 0;
char * output_file;

extern int gnoll_errno;
extern struct macro_struct *macros;
pcg32_random_t rng;

// Function Signatures for this file
int initialize();

// Functions
int initialize(){
    if (!seeded){
        unsigned long int tick = (unsigned long)time(0)+(unsigned long)clock();
        pcg32_srandom_r(
            &rng,
            tick ^ (unsigned long int)&printf,
            54u
        );
        seeded = 1;
    }
    return 0;
}

%}


%start gnoll_entry
/* %start gnoll_statement */

%token NUMBER SIDED_DIE FATE_DIE REPEAT SIDED_DIE_ZERO
%token EXPLOSION IMPLOSION PENETRATE ONCE
%token MACRO_ACCESSOR MACRO_STORAGE SYMBOL_SEPERATOR ASSIGNMENT
%token KEEP_LOWEST KEEP_HIGHEST DROP_LOWEST DROP_HIGHEST
%token FILTER
%token LBRACE RBRACE PLUS MINUS MULT MODULO DIVIDE_ROUND_UP DIVIDE_ROUND_DOWN
%token REROLL
%token SYMBOL_LBRACE SYMBOL_RBRACE STATEMENT_SEPERATOR CAPITAL_STRING
%token DO_COUNT UNIQUE IS_EVEN IS_ODD
%token RANGE
%token FN_MAX FN_MIN FN_ABS FN_POOL

/* Defines Precedence from Lowest to Highest */
%left SYMBOL_SEPERATOR STATEMENT_SEPERATOR
%left PLUS MINUS
%left MULT DIVIDE_ROUND_DOWN DIVIDE_ROUND_UP MODULO
%left KEEP_LOWEST KEEP_HIGHEST DROP_HIGHEST DROP_LOWEST
%left UMINUS
%left LBRACE RBRACE
%left EXPLOSION
%left NE EQ GT LT LE GE

%union{
    vec values;
}
/* %type<die> DIE; */
/* %type<values> NUMBER; */

%%
/* Rules Section */

gnoll_entry:
    gnoll_statement{
        // printf("A: %i\n", new_vector->content[0]);
        free_vector($<values>1);
    }
;

gnoll_statement:
    gnoll_statement STATEMENT_SEPERATOR gnoll_statement
    |
    /* Allow ending with ; */
    gnoll_statement STATEMENT_SEPERATOR
    |
    sub_statement
    |
    error {
        printf("Invalid Notation\n");
        gnoll_errno = SYNTAX_ERROR;
        YYABORT;
        yyclearin;
    }
;

sub_statement:
    macro_statement
    |
    dice_statement
;


macro_statement:
    MACRO_STORAGE CAPITAL_STRING ASSIGNMENT math{
        /**
        *
        * returns - 0
        */
                
        vec key = $<values>2;
        vec value = $<values>4;

        register_macro(&key, &value.source);

        // Cleanup
        free_vector(key);
        free_vector(value);
        
        if(gnoll_errno){
            YYABORT;
            yyclearin;
        }
        // &$<values>$ = NULL;
    }
;

dice_statement: math{
    /**
    * functions a vector
    * return NULL
    */

    vec vector = $<values>1;
    vec new_vec;
    // vec new_vec = vector;       // Code Smell.
    //                             // Target Vector should be empty

    //  Step 1: Collapse pool to a single value if nessicary
    collapse_vector(&vector, &new_vec);
    if(gnoll_errno){
        YYABORT;
        yyclearin;
    }

    // Step 2: Output to file
    FILE *fp = NULL;

    if(write_to_file){
        fp = safe_fopen(output_file, "a+");
        if(gnoll_errno){
            YYABORT;
            yyclearin;
        }
    }

    // TODO: To Function
    for(unsigned int i = 0; i!= new_vec.length;i++){
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
    
    if (dice_breakdown){
        fprintf(fp, "\n");
    }

    if(write_to_file){
        fclose(fp);
    }
    // free_vector(new_vec);

    free_vector(vector);
    $<values>$ = new_vec;
};


math:
    FN_MAX LBRACE math SYMBOL_SEPERATOR math RBRACE{
        /** @brief performs the min(__, __) function
        * @FN_MAX the symbol "max"
        * @LBRACE the symbol "("
        * function The target vector
        * SYMBOL_SEPERATOR the symbol ","
        * function The target vector
        * @RBRACE the symbol ")"
        * return vector
        */
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        int vmax = MAXV(
            $<values>3.content[0],
            $<values>5.content[0]
        );
        new_vec.content[0] = vmax;
        $<values>$ = new_vec;
        free_vector($<values>3);
        free_vector($<values>5);
    }
    |
    FN_MIN LBRACE math SYMBOL_SEPERATOR math RBRACE{
        /** @brief performs the min(__, __) function
        * @FN_MIN the symbol "min"
        * @LBRACE the symbol "("
        * function The target vector
        * SYMBOL_SEPERATOR the symbol ","
        * function The target vector
        * @RBRACE the symbol ")"
        * return vector
        */
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        new_vec.content[0] = MINV(
            $<values>3.content[0],
            $<values>5.content[0]
        );
        $<values>$ = new_vec;
        free_vector($<values>3);
        free_vector($<values>5);
    }
    |
    FN_ABS LBRACE math RBRACE{
        /** @brief performs the abs(__) function
        * @FN_ABS the symbol "abs"
        * @LBRACE the symbol "("
        * function The target vector
        * @RBRACE the symbol ")"
        * return vector
        */
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        new_vec.content[0] = ABSV(
            $<values>3.content[0]
        );
        $<values>$ = new_vec;
        free_vector($<values>3);
    }
    |
    LBRACE math RBRACE{
        $<values>$ = $<values>2;
    }
    |
    math MULT math{
        // Collapse both sides and subtract
        vec vector1 = $<values>1;
        vec vector2 = $<values>3;

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Multiplication not implemented for symbolic dice.\n");
            gnoll_errno = NOT_IMPLEMENTED;
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = safe_calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 * v2;
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
        
        free_vector(vector1);
        free_vector(vector2);
    }
    |
    math DIVIDE_ROUND_UP math{
        // Collapse both sides and subtract
        vec vector1 = $<values>1;
        vec vector2 = $<values>3;

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Division unsupported for symbolic dice.\n");
            gnoll_errno = UNDEFINED_BEHAVIOUR;
            YYABORT;
            yyclearin;

        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = safe_calloc(sizeof(int), 1);
            if(gnoll_errno){ YYABORT; yyclearin;}
            new_vec.length = 1;
            if(v2==0){
                gnoll_errno=DIVIDE_BY_ZERO;
                new_vec.content[0] = 0;
            }else{
                new_vec.content[0] = (v1+(v2-1))/ v2;
            }
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
        
        free_vector(vector1);
        free_vector(vector2);
    }
    |
    math DIVIDE_ROUND_DOWN math{
        // Collapse both sides and subtract
        vec vector1 = $<values>1;
        vec vector2 = $<values>3;

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Division unsupported for symbolic dice.\n");
            gnoll_errno = UNDEFINED_BEHAVIOUR;
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = safe_calloc(sizeof(int), 1);
            if(gnoll_errno){
               YYABORT;
               yyclearin;
            }
            new_vec.length = 1;
            if(v2==0){
                gnoll_errno=DIVIDE_BY_ZERO;
                new_vec.content[0] = 0;
            }else{
                new_vec.content[0] = v1 / v2;
            }
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
        
        free_vector(vector1);
        free_vector(vector2);
    }
    |
    math MODULO math{
        // Collapse both sides and subtract
        vec vector1 = $<values>1;
        vec vector2 = $<values>3;

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Modulo unsupported for symbolic dice.\n");
            gnoll_errno = UNDEFINED_BEHAVIOUR;
            YYABORT;
            yyclearin;

        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = safe_calloc(sizeof(int), 1);
            if(gnoll_errno){
                YYABORT;
                yyclearin;
            }
            new_vec.length = 1;
            new_vec.content[0] = v1 % v2;
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
        
        free_vector(vector1);
        free_vector(vector2);
    }
    |
    math PLUS math{
        /** @brief
        * math vector
        * PLUS symbol "+"
        * math vector
        */
        // Collapse both sides and subtract
        vec vector1 = $<values>1;
        vec vector2 = $<values>3;

        if (
            (vector1.dtype == SYMBOLIC && vector2.dtype == NUMERIC) ||
            (vector2.dtype == SYMBOLIC && vector1.dtype == NUMERIC)
        ){
            printf("Addition not supported with mixed dice types.\n");
            gnoll_errno = UNDEFINED_BEHAVIOUR;
            YYABORT;
            yyclearin;
        } else if (vector1.dtype == SYMBOLIC){
            vec new_vec;
            unsigned int concat_length = vector1.length + vector2.length;
            new_vec.symbols = safe_calloc(sizeof(char *), concat_length);
            if(gnoll_errno){
                YYABORT;
                yyclearin;
            }
            for (unsigned int i = 0; i != concat_length; i++){
                new_vec.symbols[i] = safe_calloc(sizeof(char), MAX_SYMBOL_LENGTH);
                if(gnoll_errno){
                    YYABORT;
                    yyclearin;
                }
            }
            new_vec.length = concat_length;
            new_vec.dtype = vector1.dtype;

            concat_symbols(
                vector1.symbols, vector1.length,
                vector2.symbols, vector2.length,
                new_vec.symbols
            );
            $<values>$ = new_vec;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = safe_calloc(sizeof(int), 1);
            if(gnoll_errno){
                YYABORT;
                yyclearin;
            }
            new_vec.length = 1;
            new_vec.dtype = vector1.dtype;
            new_vec.content[0] = v1 + v2;

            $<values>$ = new_vec;
        }
        free_vector(vector1);
        free_vector(vector2);

    }
    |
    math MINUS math{
        vec vector1 = $<values>1;
        vec vector2 = $<values>3;
        if (
            (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC)
        ){
            // It's not clear whether {+,-} - {-, 0} should be {+} or {+, 0}!
            // Therfore, we'll exclude it.
            printf("Subtract not supported with symbolic dice.\n");
            gnoll_errno = UNDEFINED_BEHAVIOUR;
            YYABORT;
            yyclearin;;
        }else{
            // Collapse both sides and subtract

            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = safe_calloc(sizeof(int), 1);
            if(gnoll_errno){
                YYABORT;
                yyclearin;
            }
            new_vec.length = 1;
            new_vec.content[0] = v1 - v2;
            new_vec.dtype = vector1.dtype;

            $<values>$ = new_vec;
        }
        free_vector(vector1);
        free_vector(vector2);

    }
    |
    MINUS math %prec UMINUS{
        /**
        * MINUS a symbol '-'
        * math a vector
        */
        // Eltwise Negation
        vec vector = $<values>2;

        if (vector.dtype == SYMBOLIC){
            printf("Symbolic Dice, Cannot negate. Consider using Numeric dice or post-processing.\n");
            gnoll_errno = UNDEFINED_BEHAVIOUR;
            YYABORT;
            yyclearin;;
        } else {
            vec new_vec;

            new_vec.content = safe_calloc(sizeof(int), vector.length);
            if(gnoll_errno){
                YYABORT;
                yyclearin;
            }
            new_vec.length = vector.length;
            new_vec.dtype = vector.dtype;

            for(unsigned int i = 0; i != vector.length; i++){
                new_vec.content[i] = - vector.content[i];
            }
            $<values>$ = new_vec;

        }
        free_vector(vector);
    }
    |
    collapsing_dice_operations
;

collapsing_dice_operations:
    dice_operations DO_COUNT{
        /**
        * dice_operations - a vector
        * DO_COUNT - a symbol 'c'
        */

        vec new_vec;
        vec dice = $<values>1;
        initialize_vector(&new_vec, NUMERIC, 1);

        new_vec.content[0] = (int)dice.length;
        free_vector(dice);
        $<values>$ = new_vec;
    }
    |
    dice_operations{
        /** 
        * dice_operations a vector
        * returns a vector
        */

        vec vector = $<values>1;

        if (vector.dtype == SYMBOLIC){
            // Symbolic, Impossible to collapse
            $<values>$ = vector;
        }
        else{
            // Collapse if Necessary
            if(vector.length > 1){
                vec new_vector;
                initialize_vector(&new_vector, NUMERIC, 1);
                new_vector.content[0] = sum(vector.content, vector.length);
                $<values>$ = new_vector;
                free_vector(vector);
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
            while (! check_condition(&dice, &$<values>5, (COMPARATOR)check)){
                if (count > MAX_ITERATION){
                    printf("MAX ITERATION LIMIT EXCEEDED: REROLL\n");
                    gnoll_errno = MAX_LOOP_LIMIT_HIT;
                    YYABORT; 
                    yyclearin;
                    break;
                }
                vec number_of_dice;
                initialize_vector(&number_of_dice, NUMERIC, 1);
                number_of_dice.content[0] = (int)dice.source.number_of_dice;

                vec die_sides;
                initialize_vector(&die_sides, NUMERIC, 1);
                die_sides.content[0] = (int)dice.source.die_sides;

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
            printf("No support for Symbolic die rerolling yet!\n");
            gnoll_errno = NOT_IMPLEMENTED;
            YYABORT;
            yyclearin;
        }
    }
    |
    die_roll REROLL condition NUMBER{

        vec dice = $<values>1;
        int check = $<values>3.content[0];

        if(dice.dtype == NUMERIC){
            if (check_condition(&dice, &$<values>4, (COMPARATOR)check)){

                vec number_of_dice;
                initialize_vector(&number_of_dice, NUMERIC, 1);
                number_of_dice.content[0] = (int)dice.source.number_of_dice;

                vec die_sides;
                initialize_vector(&die_sides, NUMERIC, 1);
                die_sides.content[0] = (int)dice.source.die_sides;

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
            gnoll_errno = NOT_IMPLEMENTED;
            YYABORT;
            yyclearin;;
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
            printf("No support for Symbolic die rerolling yet!\n");
            gnoll_errno = NOT_IMPLEMENTED;
            YYABORT;
            yyclearin;;
        }

    }
    |
    dice_operations FILTER singular_condition{
        vec new_vec;
        vec dice = $<values>1;
        int check = $<values>3.content[0];

        if(dice.dtype == NUMERIC){
            initialize_vector(&new_vec, NUMERIC, dice.length);
            filter(&dice, NULL, check, &new_vec);

            $<values>$ = new_vec;
        }else{
            printf("No support for Symbolic die rerolling yet!\n");
            gnoll_errno = NOT_IMPLEMENTED;
            YYABORT;
            yyclearin;;
        }

    }
    |
    dice_operations UNIQUE{
        // TODO
        vec new_vec;
        vec dice = $<values>1;

        if(dice.dtype == NUMERIC){
            initialize_vector(&new_vec, NUMERIC, dice.length);
            filter_unique(&dice, &new_vec);

            $<values>$ = new_vec;
        }else{
            printf("No support for Symbolic die rerolling yet!\n");
            gnoll_errno = NOT_IMPLEMENTED;
            YYABORT;
            yyclearin;;
        }
    }
    |
    dice_operations KEEP_HIGHEST NUMBER{
        vec keep_vector = $<values>3;
        vec new_vec;
        unsigned int num_to_hold = (unsigned int)keep_vector.content[0];

        keep_highest_values(&$<values>1, &new_vec, num_to_hold);

        $<values>$ = new_vec;
    }
    |
    dice_operations DROP_HIGHEST NUMBER{
        vec keep_vector = $<values>3;
        vec new_vec;
        unsigned int num_to_hold = (unsigned int)keep_vector.content[0];

        drop_highest_values(&$<values>1, &new_vec, num_to_hold);

        $<values>$ = new_vec;
    }
    |
    dice_operations KEEP_LOWEST NUMBER{
        vec keep_vector;
        keep_vector = $<values>3;
        unsigned int num_to_hold = (unsigned int)keep_vector.content[0];

        vec new_vec;
        keep_lowest_values(&$<values>1, &new_vec, num_to_hold);

        $<values>$ = new_vec;
    }
    |
    dice_operations DROP_LOWEST NUMBER{
        vec keep_vector;
        keep_vector = $<values>3;
        unsigned int num_to_hold = (unsigned int)keep_vector.content[0];

        vec new_vec;
        drop_lowest_values(&$<values>1, &new_vec, num_to_hold);

        $<values>$ = new_vec;
    }
    |
    dice_operations KEEP_HIGHEST{
        unsigned int num_to_hold = 1;
        vec new_vec;
        keep_highest_values(&$<values>1, &new_vec, num_to_hold);

        $<values>$ = new_vec;
    }
    |
    dice_operations DROP_HIGHEST{
        vec roll_vec = $<values>1;
        unsigned int num_to_hold = 1;

        vec new_vec;
        drop_highest_values(&roll_vec, &new_vec, num_to_hold);

        $<values>$ = new_vec;
    }
    |
    dice_operations KEEP_LOWEST{
        unsigned int num_to_hold = 1;

        vec new_vec;
        keep_lowest_values(&$<values>1, &new_vec, num_to_hold);

        $<values>$ = new_vec;
    }
    |
    dice_operations DROP_LOWEST{
        vec roll_vec = $<values>1;
        unsigned int num_to_hold = 1;

        vec new_vec;
        drop_lowest_values(&roll_vec, &new_vec, num_to_hold);

        $<values>$ = new_vec;
    }
    |
    die_roll
;

die_roll:
    NUMBER die_symbol NUMBER EXPLOSION ONCE{
        vec numA = $<values>1;
        vec ds = $<values>2;
        vec numB = $<values>3;

        int start_from = ds.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        roll_plain_sided_dice(
            &numA,
            &numB,
            &$<values>$,
            ONLY_ONCE_EXPLOSION,
            start_from
        );
        free_vector(numA);
        free_vector(ds);
        free_vector(numB);
    }
    |
    die_symbol NUMBER EXPLOSION ONCE{
        
        vec ds = $<values>1;
        vec numB = $<values>2;

        int start_from = ds.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        roll_plain_sided_dice(
            &number_of_dice,
            &numB,
            &$<values>$,
            ONLY_ONCE_EXPLOSION,
            start_from
        );
        free_vector(number_of_dice);
        free_vector(ds);
        free_vector(numB);
    }
    |
    NUMBER die_symbol NUMBER EXPLOSION PENETRATE{

        vec numA = $<values>1;
        vec ds = $<values>2;
        vec numB = $<values>3;
        int start_from = ds.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        roll_plain_sided_dice(
            &numA,
            &numB,
            &$<values>$,
            PENETRATING_EXPLOSION,
            start_from
        );
        
        free_vector(numA);
        free_vector(ds);
        free_vector(numB);
    }
    |
    die_symbol NUMBER EXPLOSION PENETRATE{
        vec ds = $<values>1;
        vec numB = $<values>2;
        
        int start_from = ds.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        roll_plain_sided_dice(
            &number_of_dice,
            &numB,
            &$<values>$,
            PENETRATING_EXPLOSION,
            start_from
        );
        free_vector(number_of_dice);
        free_vector(ds);
        free_vector(numB);
    }
    |
    NUMBER die_symbol NUMBER EXPLOSION{

        vec numA = $<values>1;
        vec ds = $<values>2;
        vec numB = $<values>3;
        int start_from = ds.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        roll_plain_sided_dice(
            &numA,
            &numB,
            &$<values>$,
            PENETRATING_EXPLOSION,
            start_from
        );
        free_vector(numA);
        free_vector(ds);
        free_vector(numB);
    }
    |
    die_symbol NUMBER EXPLOSION{

        vec ds = $<values>1;
        vec numB = $<values>2;
        int start_from = ds.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;
        
        roll_plain_sided_dice(
            &number_of_dice,
            &numB,
            &$<values>$,
            STANDARD_EXPLOSION,
            start_from
        );
        free_vector(numB);
        free_vector(ds);
        free_vector(number_of_dice);
    }
    |
    NUMBER die_symbol NUMBER{
        vec numA = $<values>1;
        vec ds = $<values>2;
        vec numB = $<values>3;
        int start_from = ds.content[0];

        roll_plain_sided_dice(
            &numA,
            &numB,
            &$<values>$,
            NO_EXPLOSION,
            start_from
        );
        free_vector(numB);
        free_vector(ds);
        free_vector(numA);
    }
    |
    die_symbol NUMBER{
        vec ds = $<values>1;
        vec numB = $<values>2;
        vec new_vec;

        int start_from = ds.content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        roll_plain_sided_dice(
            &number_of_dice,
            &numB,
            &new_vec,
            NO_EXPLOSION,
            start_from
        );
        $<values>$ = new_vec;
        free_vector(number_of_dice);
        free_vector(ds);
        free_vector(numB);

    }
    |
    NUMBER die_symbol MODULO{
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 100;

        roll_plain_sided_dice(
            &$<values>1,
            &dice_sides,
            &$<values>$,
            NO_EXPLOSION,
            1
        );
    }
    |
    die_symbol MODULO{

        vec num_dice;
        initialize_vector(&num_dice, NUMERIC, 1);
        num_dice.content[0] = 1;
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 100;

        roll_plain_sided_dice(
            &num_dice,
            &dice_sides,
            &$<values>$,
            NO_EXPLOSION,
            1
        );
    }
    |
    NUMBER die_symbol DO_COUNT{

        int start_from = $<values>2.content[0];

        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 2;

        roll_plain_sided_dice(
            &$<values>1,
            &dice_sides,
            &$<values>$,
            NO_EXPLOSION,
            start_from
        );
    }
    |
    die_symbol DO_COUNT{
        int start_from = $<values>1.content[0];

        vec num_dice;
        initialize_vector(&num_dice, NUMERIC, 1);
        num_dice.content[0] = 1;
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 2;

        roll_plain_sided_dice(
            &num_dice,
            &dice_sides,
            &$<values>$,
            NO_EXPLOSION,
            start_from
        );
    }
    |
    NUMBER FATE_DIE{
        vec result_vec;
        initialize_vector(&result_vec, SYMBOLIC, (unsigned int)$<values>1.content[0]);

        roll_symbolic_dice(
            &$<values>1,
            &$<values>2,
            &result_vec
        );
        $<values>$ = result_vec;
    }
    |
    FATE_DIE{
        vec result_vec;
        vec number_of_dice;
        initialize_vector(&result_vec, SYMBOLIC, 1);
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        roll_symbolic_dice(
            &number_of_dice,
            &$<values>1,
            &result_vec
        );
        $<values>$ = result_vec;
    }
    |
    custom_symbol_dice
    |
    NUMBER
    ;


custom_symbol_dice:
    NUMBER die_symbol SYMBOL_LBRACE csd SYMBOL_RBRACE
    {
        /**
        * NUMBER - vector
        * die_symbol - vector
        * SYMBOL_LBRACE - the symbol {
        * csd - vector
        * SYMBOL_RBRACE - the symbol }
        */
        // Nd{SYMB}
        vec left = $<values>1;
        vec dsymb = $<values>2;
        vec right = $<values>4;

        // TODO: Multiple ranges

        vec result_vec;
        initialize_vector(&result_vec, SYMBOLIC, (unsigned int)$<values>1.content[0]);

        roll_symbolic_dice(
            &left,
            &right,
            &result_vec
        );
        
        free_vector(left);
        free_vector(right);
        free_vector(dsymb);
        $<values>$ = result_vec;
    }
    |
    die_symbol SYMBOL_LBRACE csd SYMBOL_RBRACE
    {
        /** @brief 
        * @param die_symbol a vector
        * @param SYMBOL_LBRACE the symbol "{"
        * @param csd a vector
        * @param SYMBOL_LBRACE the symbol "}"
        * returns a vector
        */
        vec csd_vec = $<values>3;
        vec number_of_dice;
        vec result_vec;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;
        
        if (csd_vec.dtype == NUMERIC){
            vec dice_sides;
            vec num_dice;
            initialize_vector(&dice_sides, NUMERIC, 1);
            initialize_vector(&num_dice, NUMERIC, 1);
            initialize_vector(&result_vec, NUMERIC, 1);
            num_dice.content[0] = 1;

            int start_value = csd_vec.content[0];
            int end_value = csd_vec.content[csd_vec.length-1];
            dice_sides.content[0] = end_value - start_value + 1;

            // Range
            roll_plain_sided_dice(
                &num_dice,
                &dice_sides,
                &result_vec,
                NO_EXPLOSION,
                start_value
            );
            free_vector(dice_sides);
            free_vector(num_dice);
        }else{
            initialize_vector(&result_vec, SYMBOLIC, 1);

            roll_params rp = {
                .number_of_dice=(unsigned int)number_of_dice.content[0],
                .die_sides=csd_vec.length,
                .dtype=SYMBOLIC,
                .start_value=0,
                .symbol_pool=(char **)safe_calloc(csd_vec.length , sizeof(char *))
            };
            result_vec.source = rp;
            result_vec.has_source = true;
            for(unsigned int i = 0; i != csd_vec.length; i++){
                result_vec.source.symbol_pool[i] = malloc(MAX_SYMBOL_LENGTH);
                memcpy(
                    result_vec.source.symbol_pool[i], 
                    csd_vec.symbols[i], 
                    MAX_SYMBOL_LENGTH*sizeof(char)
                );
            }

            // Custom Symbol
            roll_symbolic_dice(
                &number_of_dice,
                &csd_vec,
                &result_vec
            );
        }

        free_vector(number_of_dice);
        free_vector(csd_vec);
        free_vector($<values>1);
        $<values>$ = result_vec;
    }
    |
    MACRO_ACCESSOR CAPITAL_STRING{
        /**
        * MACRO_ACCESSOR the symbol '@'
        * CAPITAL_STRING A vector containing a macro identifier
        * return A vector containing rollparams for the selected  macro
        */
        vec vector = $<values>2;
        char * name = vector.symbols[0];

        vec new_vector;
        search_macros(name, &new_vector.source);
        if(gnoll_errno){YYABORT;yyclearin;}
        // Resolve Roll

        vec number_of_dice;
        vec die_sides;

        // Set Num Dice
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = (int)new_vector.source.number_of_dice;
        
        // Set Die Sides
        light_initialize_vector(&die_sides, NUMERIC, 1);
        die_sides.content[0] = (int)new_vector.source.die_sides;
        die_sides.length = new_vector.source.die_sides;
        die_sides.symbols = NULL;

        // Roll according to the stored values
        // Careful: Newvector used already
        if (new_vector.source.dtype == NUMERIC){
            initialize_vector(&new_vector, new_vector.source.dtype, 1);
            roll_plain_sided_dice(
                &number_of_dice,
                &die_sides,
                &new_vector,
                new_vector.source.explode,
                1
            );
        }else if (new_vector.source.dtype == SYMBOLIC){
            free_2d_array(&die_sides.symbols, die_sides.length);
            safe_copy_2d_chararray_with_allocation(
                &die_sides.symbols,
                new_vector.source.symbol_pool,
                die_sides.length,
                MAX_SYMBOL_LENGTH
            );

            initialize_vector(&new_vector, new_vector.source.dtype, 1);
            roll_symbolic_dice(
                &number_of_dice,
                &die_sides,
                &new_vector
            );
        }else{
            printf("Complex Dice Equation. Only dice definitions supported. No operations\n");
            gnoll_errno = NOT_IMPLEMENTED;
        }
        free_vector(vector);
        free_vector(number_of_dice);
        free_vector(die_sides);
        $<values>$ = new_vector;
    }
    ;
csd:
    csd SYMBOL_SEPERATOR csd{
        /**
        * csd a vector containing custom symbols
        * SYMBOL_SEPERATOR the symbol ','
        * csd a vector containing custom symbols
        * return A vector with all the symbols
        */
        vec l = $<values>1;
        vec r = $<values>3;

        vec new_vector;
        initialize_vector(&new_vector, SYMBOLIC, l.length + r.length);

        concat_symbols(
            l.symbols, l.length,
            r.symbols, r.length,
            new_vector.symbols
        );
        free_vector(l);
        free_vector(r);
        $<values>$ = new_vector;
    }
    |
    NUMBER RANGE NUMBER{
        /**
        * NUMBER The symbol 0-9+
        * RANGE The symbol '..'
        * NUMBER The symbol 0-9+
        * return A vector containing the numeric values as symbols 
        */
        vec start = $<values>1;
        vec end = $<values>3;

        int s = start.content[0];
        int e = end.content[0];


        if (s > e){
            printf("Range: %i -> %i\n", s, e);
            printf("Reversed Ranged not supported yet.\n");
            gnoll_errno = NOT_IMPLEMENTED;
            YYABORT;
            yyclearin;
        }

        // How many values in this range:
        // 2..2 = 1 
        // 2..3 = 2
        // etc.
        unsigned int spread = (unsigned int)e - (unsigned int)s + 1; 

        vec new_vector;
        initialize_vector(&new_vector, SYMBOLIC, spread);
        for (int i = 0; i <= (e-s); i++){
            sprintf(new_vector.symbols[i], "%d", s+i);
        }
        $<values>$ = new_vector;
    }
    |
    CAPITAL_STRING
    | 
    NUMBER{
        /**
        * NUMBER The symbol 0-9+
        * return A vector containing the numeric values as symbols 
        */
        vec in = $<values>1;
        // INT_MAX/INT_MIN has 10 characters
        in.symbols = safe_calloc(1, sizeof(char *));  
        in.symbols[0] = safe_calloc(10, sizeof(char));  
        sprintf(in.symbols[0], "%d", in.content[0]);
        free(in.content);
        in.dtype = SYMBOLIC;
        $<values>$ = in;
    }
    ;

singular_condition: UNIQUE | IS_ODD | IS_EVEN ;
condition: EQ | LT | GT | LE | GE | NE ;

die_symbol:
    SIDED_DIE{
        /**
        * @brief SIDED_DIE The symbol 'd'
        * @param return A vector containing '1', the start index
        */
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        new_vec.content[0] = 1;
        $<values>$ = new_vec;
    }
    |
    SIDED_DIE_ZERO{
        /**
        * SIDED_DIE The symbol 'z'
        * return A vector containing '0', the start index
        */
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        new_vec.content[0] = 0;
        $<values>$ = new_vec;
    }
;



%%
/* Subroutines */

typedef struct yy_buffer_state * YY_BUFFER_STATE;
extern YY_BUFFER_STATE yy_scan_string(char * str);
extern void yy_delete_buffer(YY_BUFFER_STATE buffer);

int roll_full_options(
    char* roll_request, 
    char* log_file, 
    int enable_verbosity, 
    int enable_introspection,
    int enable_mocking,
    int enable_builtins,
    int mocking_type,
    int mocking_seed
){
    /**
    * @brief the main GNOLL roll function
    * @param roll_request the dice notation to parse
    * @param log_file the file location to write results to
    * @param enable_verbosity Adds extra prints to the program
    * @param enable_introspection Adds per-dice breakdown in the output file
    * @param enable_mocking Replaces random rolls with predictables values for testing
    * @param enable_builtins Load in predefined macros for usage
    * @param mocking_type Type of mock values to generate
    * @param mocking_seed The first value of the mock generation to produce
    * @return GNOLL error code
    */
    gnoll_errno = 0;

    if (enable_verbosity){
        verbose = 1;
        printf("Trying to roll '%s'\n", roll_request);
    }
    if (enable_mocking){
        init_mocking((MOCK_METHOD)mocking_type, mocking_seed);
    }
    if (log_file != NULL){
        write_to_file = 1;
        output_file = log_file;
        if (enable_introspection){
            dice_breakdown = 1;
        }
    }else{
        if (enable_introspection){
            // Introspection is only implemented on a file-basis
            gnoll_errno = NOT_IMPLEMENTED;
            return gnoll_errno;
        }
    }

    initialize();
    
    enable_builtins = 0;

    if(enable_builtins){
        load_builtins("builtins/");
    }
    
    YY_BUFFER_STATE buffer = yy_scan_string(roll_request);
    yyparse();
    yy_delete_buffer(buffer);
    return gnoll_errno;
}

void load_builtins(char* root){

    int db_setting = dice_breakdown;
    dice_breakdown = 0; // Dont want dice breakdown for all the macro loading

    tinydir_dir dir = (tinydir_dir){0};
    tinydir_open(&dir, root);
    
    int count = 0;
    while (dir.has_next)
    {
        tinydir_file file;
        tinydir_readfile(&dir, &file);
        if(verbose){
            printf("%s", file.name);
        }
        if (file.is_dir)
        {
            if(verbose){
                printf("/\n");
            }
        }else{
            count++;
            if(verbose){
               printf("\n");
            }
            
            unsigned long max_file_path_length = 1000;
            int max_macro_length = 1000;

            char* path = safe_calloc(sizeof(char), max_file_path_length);
            char* stored_str = safe_calloc(sizeof(char), (unsigned long)max_macro_length);
            if(gnoll_errno){return;}

            // Get full path
            strcat(path, "builtins/");
            strcat(path, file.name);
            
            // TODO: Check filename for length
            FILE* fp = fopen(path, "r");
            while (fgets(stored_str, max_macro_length, fp)!=NULL);

            if(verbose){
              printf("Contents: %s\n",stored_str); 
            }
            fclose(fp);
            
            YY_BUFFER_STATE buffer = yy_scan_string(stored_str);
            yyparse();
            yy_delete_buffer(buffer);
            if(gnoll_errno){return;}

            free(path);
            free(stored_str);
        }
        if(count >= 1){
            break;
        }
        tinydir_next(&dir);
    }

    tinydir_close(&dir);
    dice_breakdown = db_setting;
    return;
}

// The following are legacy functions to be deprecated in the future
// in favor of the general roll_full_options() fn.

int roll(char * s){
    return roll_full_options(s, NULL, 1, 0, 0, 0, 0, 0);
}

int roll_with_breakdown(char * s, char* f){
    return roll_full_options(s, f, 0, 1, 0, 0, 0, 0);
}

int roll_and_write(char* s, char* f){
    return roll_full_options(s, f, 0, 0, 0, 0, 0, 0);
}

void roll_and_write_R(int* return_code, char** s, char** f){    
    (*return_code) = roll_full_options(s[0], f[0], 0, 0, 0, 0, 0, 0);
}

int mock_roll(char * s, char * f, int mock_value, int mock_const){
    return roll_full_options(s, f, 0, 0, 1, 0, mock_value, mock_const);
}

int main(int argc, char **str){
    // Join arguments if they came in as seperate strings
    char * s = concat_strings(&str[1], (unsigned int)(argc - 1));

    remove("output.dice");
    roll_full_options(
        s,
        "output.dice",
        1,  // Verbose
        1,  // Introspect
        0,  // Mocking
        1,  // Builtins
        0,
        0
    );
    print_gnoll_errors();
    FILE  *f = fopen("output.dice","r");
    int c;
    printf("Result:\n");
    if (f){
        while((c = getc(f)) !=  EOF){
            putchar(c);
        }
        fclose(f);
    }
    // Final Freeing
    free(macros);
}

int yyerror(s)
const char *s;
{
    fprintf(stderr, "%s\n", s);

    if(write_to_file){
        FILE *fp;
        fp = safe_fopen(output_file, "a+");
        fprintf(fp, "%s;", s);
        fclose(fp);
    }
    return(gnoll_errno);

}

int yywrap(){
    return (1);
}

