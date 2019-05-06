
grammar dice ;

//TODO:
// Some INTEGER_NUMBERS should allow negative numbs

schema : assignment* sequence (',' sequence)* ;

assignment : STRING WSPACE? '=' WSPACE? dice_roll WSPACE? ';' ;

sequence : WSPACE? dice_roll WSPACE? duplicate? WSPACE?  ;

duplicate : 'x' INTEGER_NUMBER;

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
    (amount? die faces die_modifiers ) | 
    amount;

die_modifiers : (subset | reroll | bang | force )?;

bang : explode | implode ;

explode : condition? '!'+ ;
implode : condition? 'i'+ ;

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
        ('F'|'f') #FateFace | 
        OPEN_BRACE numeric_sequence CLOSE_BRACE #CustomFace ;

numeric_sequence : numeric_item (',' numeric_item)*;

numeric_item : seq_item | INTEGER_NUMBER ;

seq_item : INTEGER_NUMBER '..' INTEGER_NUMBER ;

// Symbols
die     : 'd';


PLUS    : '+';
POWER   : '^';
MINUS   : '-';
MULT    : '*';
DIV     :  '/';
DIV_RUP :  '|';
SEVERAL : 'x';

OPEN_BRACKET : '(';
CLOSE_BRACKET : ')';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';

SNHigh : ('H'|'h');
SNLow : ('L'|'l');
RNHigh : ('k'|'K'|'KH'|'kh');
RNLow : ('KL'|'kl');
RNDHigh : ('DH'|'dh'| 'Dh'| 'dH');
RNDLow : ('d'|'D'|'DL'|'dl'|'Dl' | 'dL');


// Data Types
INTEGER_NUMBER :   DIGIT+ ;
WSPACE : BLANK+; 
STRING : CHAR+;
fragment DIGIT   :   ('0'..'9');
fragment BLANK   : (' ' | '\t')+;
fragment CHAR    : ('a'..'z'|'A'..'Z');
