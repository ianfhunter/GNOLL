%module gnoll
%{
    extern int roll(char * s);
    extern int roll_verbose(char * s);
    extern int roll_and_write(char * s, char * f);
    extern int mock_roll(char * s, char * f, int mock_value, bool quiet, int mock_const);
%}

extern int roll(char * s);
extern int roll_verbose(char * s);
extern int roll_and_write(char * s, char * f);
extern int mock_roll(char * s, char * f, int mock_value, bool quiet, int mock_const);
