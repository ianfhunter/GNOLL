#include "rolls/mocking.h"

int random_fn_run_count = 0;
int global_mock_value = 0;
int secondary_mock_value = 0;
MOCK_METHOD global_mock_style = NO_MOCK;


void reset_mocking() {
  /**
   * @brief Resets various globals for test mocking
   */
  random_fn_run_count = 0;
  global_mock_value = 0;
  global_mock_style = NO_MOCK;
}
void init_mocking(MOCK_METHOD mock_style, int starting_value) {
  /**
   * @brief Initializes test mocking with given settings
   * @param mock_style How to apply mocking
   * @param starting_value Where mocking is applied, sets the value for the
   * first roll on the system
   */
  random_fn_run_count = 0;
  global_mock_value = starting_value;
  global_mock_style = mock_style;
}

void mocking_tick() {
  /**
   * @brief Every time a dice is rolled, this function is called so that the
   * mocking logic can update
   */
  switch (global_mock_style) {
    case RETURN_INCREMENTING: {
      global_mock_value = global_mock_value + 1;
      break;
    }
    case RETURN_DECREMENTING: {
      global_mock_value = global_mock_value - 1;
      break;
    }
    case RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE: {
      if (random_fn_run_count == 1) {
        secondary_mock_value = global_mock_value;
      }
      if (random_fn_run_count < 2) {
        global_mock_value = secondary_mock_value;
      } else {
        global_mock_value = 1;
      }
      break;
    }
    default:
      break;
  }
}
