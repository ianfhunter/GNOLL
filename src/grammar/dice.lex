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

[A-Z_]+ {
    vec vector;
    vector.storage.symbols = (char**)safe_malloc(sizeof(char **));
    if(gnoll_errno){yyerror("Memory Err");}

    vector.storage.symbols[0] = safe_strdup(yytext);
    if(gnoll_errno){yyerror("String Err");}

    vector.dtype = SYMBOLIC;
    vector.length = 1;
    vector.has_source = false;

    yylval.values = vector;
    return CAPITAL_STRING;
}

[0-9]+ {
    vec vector;
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}

    vector.storage.content[0] = fast_atoi(yytext);

    vector.has_source = false;
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
    char *plus, *minus;
    char *zeroA, *zeroB, *zeroC, *zeroD;
    plus = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    plus[0] = '+';

    zeroA = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    zeroA[0] = '0';
    zeroB = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    zeroB[0] = '0';
    zeroC = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    zeroC[0] = '0';
    zeroD = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    zeroD[0] = '0';

    minus = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    minus[0] = '-';

    vec vector;
    vector.dtype = SYMBOLIC;
    vector.storage.symbols = (char**)safe_malloc(sizeof(char **) * 6);
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.symbols[0] = plus;
    vector.storage.symbols[1] = zeroA;
    vector.storage.symbols[2] = zeroB;
    vector.storage.symbols[3] = zeroC;
    vector.storage.symbols[4] = zeroD;
    vector.storage.symbols[5] = minus;
    vector.length = 6;
    vector.has_source = false;
    yylval.values = vector;

    return(FATE_DIE);
}
(dF|df)\.[3-9] {
    char * plus, *minus;
    plus = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    plus[0] = '+';
    minus = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    minus[0] = '-';

    vec vector;
    vector.dtype = SYMBOLIC;
    vector.storage.symbols = (char**)safe_malloc(sizeof(char **) * 2);
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.symbols[0] = plus;
    vector.storage.symbols[1] = minus;
    vector.length = 2;
    vector.has_source = false;
    yylval.values = vector;

    return(FATE_DIE);
}
(dF|df)(\.2)? {
    char *plus, *minus, *zero;
    plus = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    plus[0] = '+';
    zero = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    zero[0] = '0';
    minus = (char *)safe_calloc(sizeof(char *),MAX_SYMBOL_LENGTH);
    if(gnoll_errno){yyerror("Memory Err");}
    minus[0] = '-';

    vec vector;
    vector.dtype = SYMBOLIC;
    vector.storage.symbols = (char**)safe_malloc(sizeof(char **) * 3);
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.symbols[0] = plus;
    vector.storage.symbols[1] = zero;
    vector.storage.symbols[2] = minus;
    vector.has_source = false;
    vector.length = 3;
    vector.has_source = false;
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
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = IS_UNIQUE;
    vector.dtype = NUMERIC;
    vector.length = 1;
    vector.has_source = false;
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
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = NOT_EQUAL;
    vector.dtype = NUMERIC;
    vector.length = 1;
    vector.has_source = false;
    yylval.values = vector;
    return NE;
}
\=\= {
    vec vector;
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    vector.has_source = false;
    yylval.values = vector;
    return EQ;
}
\< {
    vec vector;
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = LESS_THAN;
    vector.dtype = NUMERIC;
    vector.length = 1;
    vector.has_source = false;
    yylval.values = vector;
    return LT;
}
\> {
    vec vector;
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = GREATER_THAN;
    vector.dtype = NUMERIC;
    vector.has_source = false;
    vector.length = 1;
    yylval.values = vector;
    return GT;
}
\<\= {
    vec vector;
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = LESS_OR_EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    vector.has_source = false;
    yylval.values = vector;
    return(LE);
}
\>\= {
    vec vector;
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = GREATER_OR_EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    vector.has_source = false;
    yylval.values = vector;
    return(GE);
}
is_even {
    vec vector;
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = IF_EVEN;
    vector.dtype = NUMERIC;
    vector.length = 1;
    vector.has_source = false;
    yylval.values = vector;
    return(IS_EVEN);
}
is_odd {
    vec vector;
    vector.storage.content = (long long*)safe_malloc(sizeof(long long));
    if(gnoll_errno){yyerror("Memory Err");}
    vector.storage.content[0] = IF_ODD;
    vector.dtype = NUMERIC;
    vector.length = 1;
    vector.has_source = false;
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
