.PHONY: php
php: clean yacc lex compile shared
	cd src/php/ && php index.php
