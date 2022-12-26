<?php

// create FFI object
$gnoll = FFI::cdef(
    "int roll_and_write(char * roll, char *fn );",
    "libdice.so"
);

$fn = "output.dice";

unlink($fn);

$err = $gnoll->roll_and_write("3d6", $fn);

echo file_get_contents($fn);

