
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

clean:
	-rm grammar/* -r
	#alias antlr4

python:
	cd external ; make download ; cd ..
	bash ./setup_antlr.sh 4.7.2 Python3

	${ANTLR4} dice.g4 -o python/dice_tower/grammar -Dlanguage=Python3
	cd python ; make all ; cd ..

javascript: clean
	cd external ; make download ; cd ..
	# TODO - : on linux, ; on windows.
	bash ./setup_antlr.sh 4.7.2 Javascript
	npm install antlr4
	cd javascript ; make all ; cd ..

all : python
	echo ""

test : all
	cd python ; make test ; cd ..

lint :
	cd python ; make lint ; cd ..

install :
	cd external/antlr4/ ; export MAVEN_OPTS="-Xmx1G" ; mvn clean
	cd external/antlr4/ ; export MAVEN_OPTS="-Xmx1G" ; mvn -DskipTests install
	cd external/antlr4/ ; export MAVEN_OPTS="-Xmx1G" ; mvn package

yacc_clean:
	rm -rf build

yacc: yacc_clean
	mkdir -p build
	yacc -d src/grammar/dice.yacc
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h

	lex src/grammar/dice.lex
	cp lex.yy.c build/lex.yy.c

	cc build/y.tab.c build/lex.yy.c
	mv ./a.out build/dice

#	./build/dice < tests/test_calc.txt
	echo "== Python Test =="
	python3 src/python/yacc_wrapper.py
	python3 src/python/yacc_tests.py

.PHONY: clean python javascript all
