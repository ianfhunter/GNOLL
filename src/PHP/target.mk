PHP_FOLDER:= /usr/lib/php/20210902/

.PHONY: php
php: all
	cp build/dice.so src/PHP/dice.so
	echo ${PHP_FOLDER}
	sudo cp build/dice.so ${PHP_FOLDER}/dice.so
	LD_LIBRARY_PATH=$(PWD)/build/ php src/PHP/index.php
