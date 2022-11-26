%option never-interactive
%option nounput
%option noinput

%{
    #include <stdio.h>
    #include "shared_header.h"
    #include "util/safe_functions.h"
    #include "operations/conditionals.h"
    #include "y.tab.h"
    #include <assert.h>

    extern int gnoll_errno;
    void yyerror(char *s); // From YACC Code

    int fileno(FILE *stream);   // Bad practise, but solves warning in lex.yy.c for C99. It is unused in our application.
%}

%%

[ \n]+ /* Eat Whitespace */;

    /* TODO */
[A-Z_]+ {
    vec vector;
    vector.symbols = (char**)safe_malloc(sizeof(char **));
    if(gnoll_errno){yyerror("Memory Err");}

    vector.symbols[0] = safe_strdup(yytext);
    if(gnoll_errno){yyerror("String Err");}

    vector.dtype = SYMBOLIC;
    vector.length = 1;

    yylval.values = vector;
    return CAPITAL_STRING;
}

[0-9]+ {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}

    vector.content[0] = fast_atoi(yytext);

    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return NUMBER;
}

z {
    return(SIDED_DIE_ZERO);
}

d {
    return(SIDED_DIE);
}

(dF|df)\.1 {
    char * plus, *minus, *zero;
    plus = (char *)safe_malloc(sizeof(char *));
    if(gnoll_errno){yyerror("Memory Err");}
    plus = "+";
    zero = (char *)safe_malloc(sizeof(char *));
    if(gnoll_errno){yyerror("Memory Err");}
    zero = "0";
    minus = (char *)safe_malloc(sizeof(char *));
    if(gnoll_errno){yyerror("Memory Err");}
    minus = "-";

    vec vector;
    vector.dtype = SYMBOLIC;
    vector.symbols = (char**)safe_malloc(sizeof(char **) * 6);
    if(gnoll_errno){yyerror("Memory Err");}
    vector.symbols[0] = plus;
    vector.symbols[1] = zero;
    vector.symbols[2] = zero;
    vector.symbols[3] = zero;
    vector.symbols[4] = zero;
    vector.symbols[5] = minus;
    vector.length = 6;
    yylval.values = vector;

    return(FATE_DIE);
}
(dF|df)\.[3-9] {
    char * plus, *minus;
    plus = (char *)safe_malloc(sizeof(char *));
    if(gnoll_errno){yyerror("Memory Err");}
    plus = "+";
    minus = (char *)safe_malloc(sizeof(char *));
    if(gnoll_errno){yyerror("Memory Err");}
    minus = "-";

    vec vector;
    vector.dtype = SYMBOLIC;
    vector.symbols = (char**)safe_malloc(sizeof(char **) * 2);
    if(gnoll_errno){yyerror("Memory Err");}
    vector.symbols[0] = plus;
    vector.symbols[1] = minus;
    vector.length = 2;
    yylval.values = vector;

    return(FATE_DIE);
}
(dF|df)(\.2)? {
    char * plus, *minus, *zero;
    plus = (char *)safe_malloc(sizeof(char *));
    if(gnoll_errno){yyerror("Memory Err");}
    plus = "+";
    zero = (char *)safe_malloc(sizeof(char *));
    if(gnoll_errno){yyerror("Memory Err");}
    zero = "0";
    minus = (char *)safe_malloc(sizeof(char *));
    if(gnoll_errno){yyerror("Memory Err");}
    minus = "-";

    vec vector;
    vector.dtype = SYMBOLIC;
    vector.symbols = (char**)safe_malloc(sizeof(char **) * 3);
    if(gnoll_errno){yyerror("Memory Err");}
    vector.symbols[0] = plus;
    vector.symbols[1] = zero;
    vector.symbols[2] = minus;
    vector.length = 3;
    yylval.values = vector;

    return(FATE_DIE);
}

dl { return(DROP_LOWEST); }
dh { return(DROP_HIGHEST); }
kl { return(KEEP_LOWEST); }
kh { return(KEEP_HIGHEST); }
f { return(FILTER); }

[+] {
    return(PLUS);
}
[-] {
    return(MINUS);
}
[*] {
    return(MULT);
}
[%] {
    return(MODULO);
}
[/] {
    return(DIVIDE_ROUND_DOWN);
}
[\\] {
    return(DIVIDE_ROUND_UP);
}
[x] {
    return(REPEAT);
}
[r] {
    return(REROLL);
}
[#] {
    return(MACRO_STORAGE);
}
[@] {
    return(MACRO_ACCESSOR);
}
, {
    return(SYMBOL_SEPERATOR);
}
[(] {
    return(LBRACE);
}
[)] {
    return(RBRACE);
}
[\{] {
    return(SYMBOL_LBRACE);
}
[\}] {
    return(SYMBOL_RBRACE);
}
\.\. {
    return(RANGE);
}
;+ {
    return(STATEMENT_SEPERATOR);
}

c {
    return(DO_COUNT);
}
u {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = IS_UNIQUE;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return (UNIQUE);
}

    /* Explosions */
[!] {
    return(EXPLOSION);
}
e {
    return(EXPLOSION);
}
o {
    return(ONCE);
}
[p] {
    return(PENETRATE);
}

    /* Comparitors */
\!\= {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = NOT_EQUAL;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return NE;
}
\=\= {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return EQ;
}
\< {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = LESS_THAN;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return LT;
}
\> {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = GREATER_THAN;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return GT;
}
\<\= {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = LESS_OR_EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return(LE);
}
\>\= {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = GREATER_OR_EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return(GE);
}
is_even {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = IF_EVEN;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return(IS_EVEN);
}
is_odd {
    vec vector;
    vector.content = (int*)safe_malloc(sizeof(int));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.content[0] = IF_ODD;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return(IS_ODD);
}
    /* Macros*/
[\=] {
    return(ASSIGNMENT);
}
[~] {
    return(IMPLOSION);
}

    /*         Builtin Functions        */
    /* These should be limited in scope */

max {
    return (FN_MAX);
}
min {
    return (FN_MIN);
}
abs {
    return (FN_ABS);
}
pool {
    return (FN_POOL);
}
