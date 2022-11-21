PHP_FOLDER:= /usr/lib/php/20210902/

.PHONY: php
php: clean yacc lex compile shared
	cp build/dice.so src/PHP/dice.so
	echo ${PHP_FOLDER}
	cp build/dice.so ${PHP_FOLDER}/dice.so
	cd src/PHP/ && php index.php
