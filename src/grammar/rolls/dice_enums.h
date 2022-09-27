#ifndef __DICE_ENUMS_H__
#define __DICE_ENUMS_H__

typedef enum {
    // 0 is invalid
    SYMBOLIC=1,
    NUMERIC=2
} DIE_TYPE;

typedef enum {
    NO_EXPLOSION=0,
    STANDARD_EXPLOSION=1,
    ONLY_ONCE_EXPLOSION=2,
    PENETRATING_EXPLOSION=3,
    DIMINISHING_EXPLOSION=4
} EXPLOSION_TYPE;

#endif