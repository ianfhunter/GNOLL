---
title: Error Codes
published: true
parent: Technical Information
nav_order: 13
---

# Error Codes

| Error Value | Enum Name | Meaning |
| ----------- | --------- | ------- |
| 0           | SUCCESS   | GNOLL Completed Successfully |
| 1           | BAD_ALLOC | Issue with memory allocation            |
| 2           | BAD_FILE  | Issue with file read/writing         |
| 3           | NOT_IMPLEMENTED | Feature not Implemented yet |
| 4           | INTERNAL_ASSERT | Internal Assertion (Should not be encountered. Please file a bug) |
| 5           | UNDEFINED_BEHAVIOUR | Feature not defined. Faulty Statement |
| 6           | BAD_STRING | Issue with string functions |
| 7           | OUT_OF_RANGE | Value over max or under min of numeric range|
| 8           | IO_ERROR | Issue with printing |
| 9           | MAX_LOOP_LIMIT_HIT | Looping / Recursion Limit reached |
| 10          | SYNTAX_ERROR | The dice notation cannot be parsed and is likely malformed |
| 11          | DIVIDE_BY_ZERO | Division by zero cannot be done |
| 12          | UNDEFINED_MACRO | Attempt to access macro that was not defined | 
