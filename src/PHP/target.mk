
export PHP_FOLDER=$(php -i | grep extension_dir)
# | cut -d " " -f 5)

.PHONY: php
php: clean yacc lex compile shared
	cp build/dice.so src/PHP/dice.so
	echo ${PHP_FOLDER}
	echo $(whereis php)
	echo $(php -i)
	cp build/dice.so ${PHP_FOLDER}/dice.so
	cd src/PHP/ && php index.php
