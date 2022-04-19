%{
    #include <stdio.h>
    #include "shared_header.h"
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
kl|dh|l {
    return(KEEP_LOWEST);
}
kh|dl|h {
    return(KEEP_HIGHEST);
}

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
[p] {
    return(PENETRATE);
}
[r] {
    return(REROLL_IF);
}
[#] {
    return(MACRO_STORAGE);
}
[@] {
    return(MACRO_ACCESSOR);
}
; {

    return(MACRO_SEPERATOR);
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
[,] {
    return(SYMBOL_SEPERATOR);
}
[!] {
    return(EXPLOSION);
}
    /* Comparitors */
\!\= {
    return(NE);
}
\=\= {
    return(EQ);
}
\< {
    return(LT);
}
\> {
    return(GT);
}
\<\= {
    return(LE);
}
\>\= {
    return(GE);
}
    /* Macros*/
[\=] {
    return(ASSIGNMENT);
}
[~] {
    return(IMPLOSION);
}
