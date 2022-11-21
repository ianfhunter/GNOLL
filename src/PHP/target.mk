.PHONY: php
php: clean yacc lex compile shared
	cd src/PHP/ && php index.php
