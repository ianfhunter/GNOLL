<?php

echo 'Hello, GNOLL!';

//if (!extension_loaded('dice')) {
//  dl('dice');
//}
//roll_and_write('d300', 'output.die');



// create FFI object
$gnoll = FFI::cdef(
    "int roll_and_write(char * roll, char *fn );", 
    "libdice.so"
);

$gnoll->roll_and_write("3d6", "output.dice");

