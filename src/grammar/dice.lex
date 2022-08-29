%{
    #include <stdio.h>
    #include "shared_header.h"
    #include "rolls/condition_checking.h"
    #include "y.tab.h"
%}

%%

[ \n]+ /* Eat Whitespace */;

    /* TODO */
[A-Z_]+ {
    vec vector;
    vector.symbols = malloc(sizeof(char **));
    vector.symbols[0] = strdup(yytext);
    vector.dtype = SYMBOLIC;
    vector.length = 1;

    yylval.values = vector;
    return CAPITAL_STRING;
}

[0-9]+ {
    vec vector;
    vector.content = malloc(sizeof(int));
    vector.content[0] = atoi(yytext);
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
df|dF {
    char * plus, *minus, *zero;
    plus = (char *)malloc(sizeof(char *));
    plus = "+";
    zero = (char *)malloc(sizeof(char *));
    zero = "0";
    minus = (char *)malloc(sizeof(char *));
    minus = "-";

    vec vector;
    vector.dtype = SYMBOLIC;
    vector.symbols = malloc(sizeof(char **) * 3);
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
; {
    return(STATEMENT_SEPERATOR);
}

c {
    return(DO_COUNT);
}
u {
    return (MAKE_UNIQUE);
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
    vector.content = malloc(sizeof(int));
    vector.content[0] = NOT_EQUAL;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return NE;
}
\=\= {
    vec vector;
    vector.content = malloc(sizeof(int));
    vector.content[0] = EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return EQ;
}
\< {
    vec vector;
    vector.content = malloc(sizeof(int));
    vector.content[0] = LESS_THAN;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return LT;
}
\> {
    vec vector;
    vector.content = malloc(sizeof(int));
    vector.content[0] = GREATER_THAN;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return GT;
}
\<\= {
    vec vector;
    vector.content = malloc(sizeof(int));
    vector.content[0] = LESS_OR_EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return(LE);
}
\>\= {
    vec vector;
    vector.content = malloc(sizeof(int));
    vector.content[0] = GREATER_OR_EQUALS;
    vector.dtype = NUMERIC;
    vector.length = 1;
    yylval.values = vector;
    return(GE);
}
    /* Macros*/
[\=] {
    return(ASSIGNMENT);
}
[~] {
    return(IMPLOSION);
}
