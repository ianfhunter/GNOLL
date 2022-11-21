.PHONY: php
php: clean yacc lex compile shared
	cp build/dice.so src/PHP/dice.so
	cd src/PHP/ && php index.php
