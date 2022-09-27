%module gnoll
%{
    extern int roll(char * s);
    extern int roll_verbose(char * s);
    extern int roll_and_write(char * s, char * f);
    extern int mock_roll(char * s, char * f, int mock_value, bool quiet, int mock_const);
%}

/**
 * @brief   Roll dice and print to screen.
 * 
 * @param s Dice Notation to roll
 * @return int Exit Code
 */
extern int roll(char * s);

/**
 * @brief Roll dice and write to file.
 * 
 * @param s Dice notation to roll
 * @param f File to write result to
 * @return int Exit Code
 */
extern int roll_and_write(char * s, char * f);
/**
 * @brief Test Function for rolling dice
 * 
 * @param s Dice notation to roll
 * @param f File to write result to
 * @param mock_value Mocking Style to use (Enum)
 * @param quiet Boolean for verbosity
 * @param mock_const If using mocking, what value to start with
 * @return int Exit Code
 */
extern int mock_roll(char * s, char * f, int mock_value, int quiet, int mock_const);
