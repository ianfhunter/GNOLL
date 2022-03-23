%{
    #include <stdio.h>
    #include "y.tab.h"
    #include "shared_header.h"
%}

%%


[ \n]+ /* Eat Whitespace */;

-?[0-9]+ {
    vec vector;
    vector.content = malloc(sizeof(int));
    vector.content[0] = atoi(yytext);
    vector.length = 1;
    yylval.values = vector;
    return NUMBER;
}

d {
    return(SIDED_DIE);
}
df|dF {
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
