%{
    #include <stdio.h>
    #include "y.tab.h"
    #include "shared_header.h"
%}

%%

[ \n]+ /* Eat Whitespace */;

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
    plus[0] = '+';
    zero = (char *)malloc(sizeof(char *));
    zero[0] = '0';
    minus = (char *)malloc(sizeof(char *));
    minus[0] = '-';

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
[#] {
    return(MACRO_STORAGE);
}
[@] {
    return(MACRO_ACCESSOR);
}
[(] {
    return(LBRACE);
}
[)] {
    return(RBRACE);
}
[!] {
    return(EXPLOSION);
}
[~] {
    return(IMPLOSION);
}
