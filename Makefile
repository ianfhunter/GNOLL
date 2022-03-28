.PHONY: clean
clean:
	rm -rf build
	rm src/grammar/test_dice.yacc | true

.PHONY: yacc
yacc:
	mkdir -p build
	# yacc -d src/grammar/dice.yacc
	yacc -d src/grammar/dice.yacc --debug --verbose
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h
	mv y.output build/y.output | true

.PHONY: mocked_yacc
mocked_yacc:
	mkdir -p build
	yacc -d src/grammar/test_dice.yacc
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h

.PHONY: lex
lex:
	lex src/grammar/dice.lex
	mv lex.yy.c build/lex.yy.c

.PHONY: compile
compile:
	cc build/y.tab.c build/lex.yy.c -Isrc/grammar/
# Linux
	mv ./a.out build/dice | true
# Windows
	mv ./a.exe build/dice | true

.PHONY: all
all: clean yacc lex compile
	echo "== Build Complete =="

.PHONY: mock
mock: mocked_yacc lex compile
	echo "== Build Complete =="

.PHONY: test
test : all
	python3 -m pytest src/python/
