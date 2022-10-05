
.PHONY: clean yacc lex compile all test test_no_pip
yacc:
	mkdir -p build
	if [ -z $(DEBUG) ]; then \
		yacc -d src/grammar/dice.yacc; \
	else \
		yacc -d src/grammar/dice.yacc --debug --verbose; \
	fi
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h
	mv y.output build/y.output | true	# Only present with verbose

lex:
	lex src/grammar/dice.lex
	mv lex.yy.c build/lex.yy.c

compile:
# Executable
	cc -O3 build/y.tab.c \
		src/grammar/rolls/sided_dice.c \
		src/grammar/rolls/condition_checking.c \
		src/grammar/vector_functions.c \
		src/grammar/dice_logic.c \
		src/grammar/macro_logic.c \
		build/lex.yy.c \
		-Isrc/grammar/

# Shared Lib
	cc -fPIC -c build/y.tab.c -o build/tab.o -Isrc/grammar/
	cc -fPIC -c src/grammar/vector_functions.c -o build/vec.o -Isrc/grammar/
	cc -fPIC -c src/grammar/dice_logic.c -o build/die.o -Isrc/grammar/
	cc -fPIC -c src/grammar/macro_logic.c -o build/macro.o -Isrc/grammar/
	cc -fPIC -c src/grammar/rolls/sided_dice.c -o build/rso.o -Isrc/grammar/
	cc -fPIC -c src/grammar/rolls/condition_checking.c -o build/cc.o -Isrc/grammar/
	cc -fPIC -c build/lex.yy.c -o build/lex.o  -Isrc/grammar/
	cc -shared -o build/dice.so build/die.o build/macro.o build/tab.o build/cc.o build/lex.o build/vec.o build/rso.o

# Linux
	mv ./a.out build/dice | true
# Windows
	mv ./a.exe build/dice | true

all: clean yacc lex compile
	echo "== Build Complete =="

test_no_pip :
	python3 -m pytest tests/python/ -x

test : pip
	python3 -m pytest tests/python/ -x

include src/python/target.mk
include src/js/target.mk
include src/go/target.mk
include src/perl/target.mk
include src/swig/target.mk
include src/haskell/target.mk

clean: perl_clean python_clean
	rm -rf build
	rm src/grammar/test_dice.yacc | true