

typedef enum {NUMERIC, SYMBOLIC, MIXED} dice_type;



int initialize();
// int resolve_dice(dice die);

int min(int * arr, int len);
int max(int * arr, int len);
void pop(int * arr, int len, int value, int * new_arr);