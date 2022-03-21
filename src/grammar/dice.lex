%{
    #include <stdio.h>
    #include "y.tab.h"
    int c;
    extern int yylval;
%}

%%


[ \n]+ /* Eat Whitespace */;

[0-9]+ {
    yylval = atoi(yytext);
    return(NUMBER);
}

[d|D] {
    return(SIDED_DIE);
}
[d|D][f|F] {
    return(FATE_DIE);
}
[l|kl|dh] {
    return(KEEP_LOWEST);
}
[h|kh|dl] {
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
    return(DIVIDE_ROUND_UP);
}
[\\] {
    return(DIVIDE_ROUND_DOWN);
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
