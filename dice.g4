
grammar dice ;

schema : WSPACE? assignment* sequence? WSPACE? EOF;

assignment : store_variable WSPACE? '=' WSPACE? dice_roll WSPACE? END_ASSIGNMENT WSPACE? ;

access_variable: ACCESSOR UPPER_CASE_STRING;
store_variable: STORAGE UPPER_CASE_STRING;

sequence :
    sequence WSPACE? ITEM_SEPERATOR WSPACE? sequence  #MultiItem |
    dice_roll #BubbleRoll;

dice_roll : alter_modifier ;

alter_modifier:
    alter_modifier bang #DoBang |
    alter_modifier count #CountSuccess |
    alter_modifier reroll #TryAgain |
    alter_modifier subset #DoSubset |
    alter_modifier force #DoForce |
    math_addsub #BubbleModifier;

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
    math_muldiv  WSPACE? MODULO WSPACE? math_muldiv #Modulo |
    math_several #BubbleSeveral;

math_several :
    // Multiple, Division
    math_several  WSPACE? SEVERAL  WSPACE? math_several #Sev |
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
    amount? (die faces | fateDie | access_variable) |
    amount;

count : '£' condition? ;

bang : (explode | implode) condition? ;

explode : '!' ;
implode : '~' ;

force : '?' condition;

condition :
    '#' INTEGER_NUMBER #exactMatch |
    '<=' INTEGER_NUMBER #lessOrEqualTo |
    '>=' INTEGER_NUMBER #greaterOrEqualTo |
    '<' INTEGER_NUMBER #lessThan |
    '>' INTEGER_NUMBER #greaterThan ;


reroll : (rr_times | rr_all) condition ;
rr_times : 'r' amount? ;
rr_all : 'rr' ;

subset : subset_standard_notation | subset_rolegate_notation; //  | subset_rolegate_drop_notation

subset_standard_notation :
    MINUS subset_size? SNLow #LowerSN |
    MINUS subset_size? SNHigh #HigherSN ;

subset_rolegate_notation :
    RNLow subset_size? #LowerRN |
    RNHigh subset_size? #HigherRN ;

// subset_rolegate_drop_notation :
//     RNDLow subset_size? #LowerRND |
//     RNDHigh subset_size? #HigherRND ;


// NUMERIC MEANINGS
subset_size : INTEGER_NUMBER;
amount : INTEGER_NUMBER ;


faces : INTEGER_NUMBER #StandardFace |
        OPEN_BRACE  WSPACE? numeric_sequence  WSPACE? CLOSE_BRACE #CustomFace ;

// numeric_sequence : numeric_item  WSPACE? (','  WSPACE? numeric_item WSPACE?)*;
numeric_sequence :
    numeric_sequence WSPACE? COMMA WSPACE? numeric_sequence #NSequence |
    numeric_item #NItem ;

numeric_item : seq_item |
               MINUS? INTEGER_NUMBER |
               (SYMBOL);

seq_item : MINUS? INTEGER_NUMBER WSPACE?  '..' WSPACE? MINUS? INTEGER_NUMBER ;


// Symbols
die     : 'd';
fateDie : ('dF' | 'df');


PLUS    : '+';
POWER   : '^';
MINUS   : '-';
MULT    : '*';
DIV     :  '/';
MODULO     :  '%';
DIV_RUP :  '|';
SEVERAL : 'x';

STORAGE : '#';
ACCESSOR: '@';

COMMA : ',';
ITEM_SEPERATOR : ':';
END_ASSIGNMENT: ';';

OPEN_BRACKET : '(';
CLOSE_BRACKET : ')';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';

SNHigh : ('h');
SNLow : ('l');
RNHigh : ('kh');
RNLow : ('kl');
// RNDHigh : ('dh');
// RNDLow : ('dl' );  // d should be preserved as key letter


// Data Types
INTEGER_NUMBER : DIGIT+ ;
WSPACE : BLANK+;


SYMBOL    : (CHESS_U | CARDS_U | ZODIAC_U | RUNIC_U | ROMAN_NUMERALS_U | MISC_U | UPCHAR);
UPPER_CASE_STRING : (UPCHAR|UNDERSCORE)+;
LOWER_CASE_STRING : LOCHAR+;
STRING : CHAR+;

fragment UPCHAR    : ('A'..'Z');
fragment UNDERSCORE: '_';
fragment LOCHAR    : ('a'..'z');


fragment DIGIT   :   ('0'..'9');
fragment BLANK   : (' ' | '\t')+;
fragment CHAR    : ('a'..'z'|'A'..'Z'|'_');

fragment CHESS_U : '\u2654'..'\u265F' ;
fragment CARDS_U : '\u2660'..'\u2667' ; // Suits
fragment ZODIAC_U : '\u2648'..'\u2653' | '\u26CE' ;
fragment RUNIC_U : '\u16A0'..'\u16FE';
fragment ROMAN_NUMERALS_U : '\u2160'..'\u217B';
fragment MISC_U : '\u2596'..'\u27EF';