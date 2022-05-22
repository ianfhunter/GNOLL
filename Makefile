.PHONY: clean
clean:
	rm -rf build
	rm src/grammar/test_dice.yacc | true
# Python Packaging can create extraoneous files
	rm src/python/src/ | true
	rm src/python/dist/ | true
	rm src/python/build/ | true
	rm src/python/LICENSE | true
	rm src/python/Makefile | true

.PHONY: yacc
yacc:
	mkdir -p build
	yacc -d src/grammar/dice.yacc 
	#yacc -d src/grammar/dice.yacc --debug --verbose
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h
	mv y.output build/y.output | true	# Only present with verbose

.PHONY: lex
lex:
	lex src/grammar/dice.lex
	mv lex.yy.c build/lex.yy.c

.PHONY: compile
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

.PHONY: all
all: clean yacc lex compile
	echo "== Build Complete =="

.PHONY: test_no_pip
test_no_pip : 
	python3 -m pytest tests/python/ -x

.PHONY: test
test : pip
	python3 -m pytest tests/python/ -x

.PHONY: pip
pip : all
	echo "----------------- BUILD -------------------------"
	cd src/python/ ; python3 -m build
	echo "------------------INSTALL------------------------"
	python3 -m pip install -vvv --user --no-index --find-links=src/python/dist/ --force-reinstall --ignore-installed dice_tower
	echo "-------------------- TEST ----------------------"
	python3 -c "from dicetower import parser as dt; dt.roll('2')"


.PHONY: publish
publish: test
	#twine upload --repository-url https://test.pypi.org/legacy/ src/python/dist/*
	twine upload src/python/dist/*
