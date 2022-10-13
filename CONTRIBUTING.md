# Contribution Guide
## How to Contribute
We're so happy you're considering contributing! Thank you! We hope this document will make it easier to do that.

## Process
Please assign yourself to a ticket, or request this, so anyone looking doesn't work on the same thing! Clone the code, make your changes, add a test & create a PR! We'll try to review it as soon as we can

## Scope
GNOLL is specifically designed to be a library for Dice Notation. What that means is, that we are looking for contributions that expand, improve or simplify parsing that notation. TTRPG character creation/storage, Encounter tracking or any other game mechanics are **out of scope** and are best handled as a wrapper around GNOLL in a seperate repository.

Similarly, GNOLL is not overly concerned about the graphical display of the results, but the actual results themselves. We may only consider these contributions on a per-case basis.

## New Language Support
We would love it if you added a language not yet on our list. We have two things for you to observe first though.

 1. Please add a test so we will know if it breaks!
 2. Try to use the existing C code, if you think there is no way to do this, please mention it in our issues/discussion tab so we can discuss alternatives. We'd really like to avoid duplicating files!
 3. Provide both a passing case AND a failing case to show our exit codes being used.

## C Guidelines
As much as possible, try to keep logic *out* of the .lex and .yacc files and in functions imported from other files.

GNOLL should ideally never crash and we control this by:

  - Writing errors to the global `gnoll_errno`
  - Checking this value is == 0 before doing any work in your function.
  - All functions that can cause memory/io issues should use safe equivilents in safe_functions.h . Where a function can produce an error code, they should immediately return.
