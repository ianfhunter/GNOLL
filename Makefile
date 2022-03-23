clean:
	rm -rf build

all: clean
	mkdir -p build
	yacc -d src/grammar/dice.yacc
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h

	lex src/grammar/dice.lex
	cp lex.yy.c build/lex.yy.c

	cc build/y.tab.c build/lex.yy.c -Isrc/grammar/
# Linux
	mv ./a.out build/dice | true
# Windows
	mv ./a.exe build/dice | true
	echo "== Build Complete =="


test : all
	python3 -m pytest src/python/yacc_tests.py


.PHONY: clean all test
