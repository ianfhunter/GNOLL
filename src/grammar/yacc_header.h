

typedef enum {NUMERIC, SYMBOLIC, MIXED} dice_type;



int initialize();
// int resolve_dice(dice die);

int min(int * arr, int len);
int max(int * arr, int len);
void pop(int * arr, int len, int value, int * new_arr);
int sum(int * arr, int len);
int collapse(int * arr, int len);
int roll_numeric_die(int small, int big);
int roll_symbolic_die(int length_of_symbolic_array);