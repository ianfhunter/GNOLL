<?php

echo 'Hello, GNOLL!';

if (!extension_loaded('dice')) {
   dl('dice');
}
roll_and_write('d300', 'output.die');