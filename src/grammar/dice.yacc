%{

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int regs[26];
int base;

int initialize(){
    srand(time(NULL));
}


int choice(int small, int big){
    return rand()%(big+1-small)+small;
}

%}


%start dice

%token NUMBER SIDED_DIE FATE_DIE PLUS MINUS MULT MODULO DIVIDE_ROUND_UP DIVIDE_ROUND_DOWN REPEAT PENETRATE KEEP_LOWEST KEEP_HIGHEST MACRO_ACCESSOR MACRO_STORAGE

/* Defines Precedence from Lowest to Highest */
%left '+' '-'
%left '*' '/' '%'
%left UMINUS

%%   /* Rules Section */

// A Die Roll Can be:
// - [x]d[y]
// - (1)d[x]
// - [x]dF
// - (1)dF
// - [x]
dice: NUMBER SIDED_DIE NUMBER
{
    int result = 0;
    for(int i = 0; i != $1; i++){
        result += choice(1, $3);
    }
    printf("%d\n", result);
    $$ = result;
}
|
SIDED_DIE NUMBER
{
    int result = choice(1, $2);
    printf("%d\n", result);
    $$ = result;
}
|
NUMBER FATE_DIE
{
    int result = 0;
    for(int i = 0; i != $1; i++){
        result += choice(-1, 1);
    }
    printf("%d\n", result);
    $$ = result;
}
|
FATE_DIE
{
    int result = choice(-1, 1);
    printf("%d\n", result);
    $$ = result;
}
|
NUMBER
;

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
