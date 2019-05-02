
grammar dice ;

// Parser rules

schema : dice_roll* ;

dice_roll : die_roll (OPERATOR dice_roll)*;

die_roll : amount die faces;


// Symbols
die     : 'd';
FATE    : 'F';

OPERATOR : PLUS | MINUS | MULT | DIV | SEVERAL;
PLUS    : '+';
MINUS   : '-';
MULT    : '*';
DIV    :  '/';
SEVERAL : 'x';

subset : amount (highest | lowest) ;
highest : 'H';
lowest  : 'L';

// NUMERIC MEANINGS
amount : INTEGER_NUMBER ;
faces : INTEGER_NUMBER ;

// Data Types
INTEGER_NUMBER :   DIGIT+ ;

fragment DIGIT   :   ('0'..'9');
