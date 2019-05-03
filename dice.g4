
grammar dice ;

// Parser rules

schema : WSPACE? dice_roll* WSPACE? ;

dice_roll : die_roll (WSPACE? OPERATOR WSPACE? dice_roll)*;

die_roll : (amount? die faces ) | amount;

// Symbols
die     : 'd';
FATE    : 'F';

OPERATOR : POWER | MULT | DIV | DIV_RUP | PLUS | MINUS | SEVERAL;

PLUS    : '+';
POWER   : '^';
MINUS   : '-';
MULT    : '*';
DIV     :  '/';
DIV_RUP :  '|';
SEVERAL : 'x';

OPEN_BRACKET : '(';
CLOSE_BRACKET : ')';

subset : amount (highest | lowest) ;
highest : 'H';
lowest  : 'L';

// NUMERIC MEANINGS
amount : INTEGER_NUMBER ;
faces : INTEGER_NUMBER ;

// Data Types
INTEGER_NUMBER :   DIGIT+ ;

fragment DIGIT   :   ('0'..'9');
fragment WSPACE : (' ' | '\t')+; 