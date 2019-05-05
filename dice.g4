
grammar dice ;

// Parser rules

schema : WSPACE? dice_roll WSPACE? ;

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
    OPEN_BRACKET  WSPACE? math_addsub WSPACE? CLOSE_BRACKET #Brackets ;

// A Die Roll Can be: 
// - NumdFace
// - dFace (implicit Num=1)
// - Value (implicit Face=1)
die_roll : (amount? die faces subset?) | amount;

subset : subset_standard_notation | subset_rolegate_notation ;

subset_standard_notation : 
    MINUS subset_size? ('L'|'l') #Lower |
    MINUS subset_size? ('H'|'h') #Higher ;

subset_rolegate_notation :  
    ('kl'|'KL') subset_size? #Lower |
    ('k'|'kh'|'K'|'KH') subset_size? #Higher ;

subset_rolegate_drop_notation :  
    ('D'|'d') subset_size? #Lower |
    ('D'|'DH'|'d'|'dh') subset_size? #Higher ;


// NUMERIC MEANINGS
subset_size : INTEGER_NUMBER;
amount : INTEGER_NUMBER ;
faces : INTEGER_NUMBER ;

// Symbols
die     : 'd';
FATE    : 'F';


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


// Data Types
INTEGER_NUMBER :   DIGIT+ ;
WSPACE : BLANK+; 
fragment DIGIT   :   ('0'..'9');
fragment BLANK   : (' ' | '\t')+;
