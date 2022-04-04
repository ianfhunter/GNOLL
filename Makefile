.PHONY: clean
clean:
	rm -rf build
	rm src/grammar/test_dice.yacc | true

.PHONY: yacc
yacc:
	mkdir -p build
	yacc -d src/grammar/dice.yacc
	# yacc -d src/grammar/dice.yacc --debug --verbose
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h
	mv y.output build/y.output | true

.PHONY: mocked_yacc
mocked_yacc:
	mkdir -p build
	yacc -d src/grammar/test_dice.yacc
	# yacc -d src/grammar/dice.yacc --debug --verbose
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h

.PHONY: lex
lex:
	lex src/grammar/dice.lex
	mv lex.yy.c build/lex.yy.c

.PHONY: compile
compile:
# Executable
	cc build/y.tab.c src/grammar/vector_functions.c build/lex.yy.c -Isrc/grammar/

# Shared Lib
	cc -fPIC -c build/y.tab.c -o build/tab.o -Isrc/grammar/
	cc -fPIC -c src/grammar/vector_functions.c -o build/vec.o -Isrc/grammar/
	cc -fPIC -c build/lex.yy.c -o build/lex.o  -Isrc/grammar/
	cc -shared -o build/dice.so  build/tab.o build/lex.o build/vec.o

	# ar rcs build/dice.a build/tab.o build/lex.o build/vec.o

# Linux
	mv ./a.out build/dice | true
# Windows
	mv ./a.exe build/dice | true

.PHONY: all
all: clean yacc lex compile
	echo "== Build Complete =="

.PHONY: mock
mock: mocked_yacc lex compile
	echo "== Mocking Complete =="

.PHONY: test
test : all  # pip
	python3 -m pytest tests/python/

.PHONY: pip
pip : all
	cd src/python/ ; python3 setup.py build
	cd src/python/ ; sudo python3 setup.py install
	cd src/python/ ; python3 setup.py sdist
	# pip install src/python/dist/DiceTower-2.1.0-py3-none-any.whl --force-reinstall
	python3 -c "import dicetower.parser as dt;dt.roll('1d2')"
