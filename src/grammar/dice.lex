%{
    #include <stdio.h>
    #include "y.tab.h"
    int c;
    extern int yylval;
%}

%%


" " ;

[0-9] {
    c = yytext[0];
    yylval = c - '0';
    return(DIGIT);
}
[^0-9\b] {
    c = yytext[0];
    return(c);
}
