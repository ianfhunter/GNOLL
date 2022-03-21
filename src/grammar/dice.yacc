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

%token DIGIT LETTER

%left '|'
%left '&'
%left '+' '-'
%left '*' '/' '%'
%left UMINUS  /*supplies precendecne for unary minus*/
%left DIE

%%   /* Rules Section */

dice: number die_symbol number
{
    int result = 0;
    for(int i = 0; i != $1; i++){
        result += choice(1, $3);
    }
    printf("%d\n", result);
}
;

die_symbol: 'd' %prec DIE
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
    number
    ;
*/

number: DIGIT{
        $$ = $1;
        base = ($1==0) ? 8: 10;
    }
    |
    number DIGIT
    {
        $$ = base * $1 + $2;
    }
    ;


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
