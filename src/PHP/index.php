<?php

// create FFI object
$gnoll = FFI::cdef(
    "int gnoll_validate_roll_request(const char *notation);
     int roll_and_write(char * roll, char *fn );",
    "libdice.so"
);

$fn = "output.dice";

unlink($fn);

$notation = "3d6";
$v = $gnoll->gnoll_validate_roll_request($notation);
if ($v !== 0) {
    die("GNOLL validate error: " . $v);
}
$err = $gnoll->roll_and_write($notation, $fn);

$myfile = fopen($fn, "r") or die("Unable to open file!");
echo fread($myfile, filesize($fn));
fclose($myfile);

