
grammar dice ;

//TODO:
// Some INTEGER_NUMBERS should allow negative numbs

schema : (assignment)* (sequence (',' sequence)*)?;

assignment : WSPACE? variable WSPACE? '=' WSPACE? dice_roll WSPACE? ';' WSPACE? ;

variable: '$' STRING;

sequence : WSPACE? dice_roll WSPACE?  ;

dice_roll : math_addsub ;

// Math needs to have a heirarchy so that BOMDAS is observed
math_addsub : 
    // Add Sub
    math_addsub  WSPACE? PLUS  WSPACE? math_addsub #Add |
    math_addsub  WSPACE? MINUS WSPACE? math_addsub #Sub |
    math_muldiv #BubbleMulDiv;   

math_muldiv : 
    // Multiple, Division
    math_muldiv  WSPACE? MULT  WSPACE? math_muldiv #Mul |
    math_muldiv  WSPACE? DIV  WSPACE? math_muldiv #DivDown |
    math_muldiv  WSPACE? DIV_RUP  WSPACE? math_muldiv #DivUp |
    math_several #BubbleSeveral;

math_several : 
    // Multiple, Division
    math_several  WSPACE? SEVERAL  WSPACE? math_several #Several |
    math_pow #BubblePow;

math_pow : 
    // Power Of
    math_pow  WSPACE? POWER  WSPACE? math_pow #Power |
    math_neg #BubbleNeg;

math_neg : 
    // Negation
    MINUS  WSPACE? math_neg  WSPACE? #Negate| 
    math_leaf #NoNegate;

math_leaf : 
    // Unit or Brackets
    die_roll #Value |
    OPEN_BRACKET WSPACE? math_addsub WSPACE? CLOSE_BRACKET #Brackets ;

// A Die Roll Can be: 
// - NumdFace
// - dFace (implicit Num=1)
// - Value (implicit Face=1)
die_roll : 
    (amount? (die faces | fateDie | variable) die_modifier* ) | 
    amount;

die_modifier : (subset | reroll | bang | force | count );

count : ('£');

bang : explode | implode ;

explode : condition? '!'+ ;
implode : condition? '~'+ ;

force : condition;

condition : 
    '#' INTEGER_NUMBER #exactMatch |
    '<=' INTEGER_NUMBER #lessOrEqualTo |
    '>=' INTEGER_NUMBER #greaterOrEqualTo |
    '<' INTEGER_NUMBER #lessThan |
    '>' INTEGER_NUMBER #greaterthan ;


reroll : condition (rr_times | rr_all);
rr_times : 'r' amount? ;
rr_all : 'R' ;

subset : subset_standard_notation | subset_rolegate_notation | subset_rolegate_drop_notation;

subset_standard_notation : 
    MINUS subset_size? SNLow #LowerSN |
    MINUS subset_size? SNHigh #HigherSN ;

subset_rolegate_notation :  
    RNLow subset_size? #LowerRN |
    RNHigh subset_size? #HigherRN ;

subset_rolegate_drop_notation :  
    RNDLow subset_size? #LowerRND |
    RNDHigh subset_size? #HigherRND ;


// NUMERIC MEANINGS
subset_size : INTEGER_NUMBER;
amount : INTEGER_NUMBER ;


faces : INTEGER_NUMBER #StandardFace | 
        WSPACE? OPEN_BRACE  WSPACE? numeric_sequence  WSPACE? CLOSE_BRACE WSPACE? #CustomFace;

numeric_sequence : numeric_item  WSPACE? (','  WSPACE? numeric_item WSPACE?)*;

numeric_item : seq_item | MINUS? INTEGER_NUMBER ;

seq_item : MINUS? INTEGER_NUMBER WSPACE?  '..' WSPACE? MINUS? INTEGER_NUMBER ;

// Symbols
die     : 'd';
fateDie : ('dF' | 'df');


PLUS    : '+';
POWER   : '^';
MINUS   : '-';
MULT    : '*';
DIV     :  '/';
DIV_RUP :  '|';
SEVERAL : '@';

OPEN_BRACKET : '(';
CLOSE_BRACKET : ')';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';

SNHigh : ('H'|'h');
SNLow : ('L'|'l');
RNHigh : ('k'|'K'|'KH'|'kh');
RNLow : ('KL'|'kl');
RNDHigh : ('DH'|'dh'| 'Dh'| 'dH');
RNDLow : ('D'|'DL'|'Dl' );  // d should be preserved as key letter


// Data Types
INTEGER_NUMBER : DIGIT+ ;
WSPACE : BLANK+; 
STRING : CHAR+;
fragment DIGIT   :   ('0'..'9');
fragment BLANK   : (' ' | '\t')+;
fragment CHAR    : ('a'..'z'|'A'..'Z'|'_');
