#ifndef __MOCKING_H__
#define __MOCKING_H__

#include "constructs/dice_enums.h"
#include "shared_header.h"


typedef enum {
  NO_MOCK = 0,
  RETURN_CONSTANT = 1,
  RETURN_INCREMENTING = 2,
  RETURN_DECREMENTING = 3,
  RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE = 4
} MOCK_METHOD;

// Mocking Util
void reset_mocking(void);
void init_mocking(MOCK_METHOD mock_style, long long starting_value);
void mocking_tick(void);

#endif
