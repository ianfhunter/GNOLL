
PHP_FOLDER=php -i | grep extension_dir  | cut -d " " -f 5

.PHONY: php
php: clean yacc lex compile shared
	cp build/dice.so src/PHP/dice.so
	cp build/dice.so /usr/lib/php/ /dice.so
	echo ${PHP_FOLDER}
	cd src/PHP/ && php index.php
