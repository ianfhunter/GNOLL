#include <errno.h>
#include <limits.h>
#include <stdlib.h>
#include <string.h>

#include "shared_header.h"
#include "util/safe_functions.h"

extern int gnoll_errno;

static int is_decimal_digit(unsigned char c) {
  return c >= (unsigned char)'0' && c <= (unsigned char)'9';
}

static int validate_decimal_runs(const char *s, size_t n) {
  size_t i = 0;
  while (i < n) {
    if (!is_decimal_digit((unsigned char)s[i])) {
      i++;
      continue;
    }
    size_t start = i;
    while (i < n && is_decimal_digit((unsigned char)s[i])) {
      i++;
    }
    if (i - start > (size_t)GNOLL_MAX_DECIMAL_TOKEN_LEN) {
      gnoll_errno = OUT_OF_RANGE;
      return -1;
    }
    errno = 0;
    char *end = NULL;
    (void)strtoll(s + start, &end, 10);
    if (errno == ERANGE || end != s + i) {
      gnoll_errno = OUT_OF_RANGE;
      return -1;
    }
  }
  return 0;
}

static int validate_xdy_patterns(const char *s, size_t n) {
  for (size_t i = 0; i < n; i++) {
    if (s[i] != 'd') {
      continue;
    }
    if (i + 1 >= n || !is_decimal_digit((unsigned char)s[i + 1])) {
      continue;
    }

    unsigned long long dice_count = 1;
    size_t prefix_start = i;
    if (prefix_start > 0 && is_decimal_digit((unsigned char)s[prefix_start - 1])) {
      while (prefix_start > 0 &&
             is_decimal_digit((unsigned char)s[prefix_start - 1])) {
        prefix_start--;
      }
      size_t plen = i - prefix_start;
      if (plen > (size_t)GNOLL_MAX_DECIMAL_TOKEN_LEN) {
        gnoll_errno = OUT_OF_RANGE;
        return -1;
      }
      errno = 0;
      char *end = NULL;
      long long cval = strtoll(s + prefix_start, &end, 10);
      if (errno == ERANGE || end != s + i || cval < 0) {
        gnoll_errno = OUT_OF_RANGE;
        return -1;
      }
      dice_count = (unsigned long long)cval;
    }

    size_t q = i + 1;
    while (q < n && is_decimal_digit((unsigned char)s[q])) {
      q++;
    }
    if (q - (i + 1) > (size_t)GNOLL_MAX_DECIMAL_TOKEN_LEN) {
      gnoll_errno = OUT_OF_RANGE;
      return -1;
    }
    errno = 0;
    char *end = NULL;
    (void)strtoll(s + i + 1, &end, 10);
    if (errno == ERANGE || end != s + q) {
      gnoll_errno = OUT_OF_RANGE;
      return -1;
    }

    if (dice_count > GNOLL_MAX_DICE_PER_ROLL) {
      gnoll_errno = MAX_LOOP_LIMIT_HIT;
      return -1;
    }
  }
  return 0;
}

int gnoll_validate_roll_request(const char *roll_request) {
  gnoll_errno = 0;
  if (roll_request == NULL) {
    gnoll_errno = BAD_STRING;
    return gnoll_errno;
  }
  size_t n = strlen(roll_request);
  if (validate_decimal_runs(roll_request, n) != 0) {
    return gnoll_errno;
  }
  if (validate_xdy_patterns(roll_request, n) != 0) {
    return gnoll_errno;
  }
  return 0;
}
