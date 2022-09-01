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
# Perl Artifacts
	rm MYMETA.json | true
	rm MYMETA.yml | true
	rm result.die | true

.PHONY: yacc
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
	# Copy Build
	rm -rf src/python/code/gnoll/c_build/
	rm -rf src/python/code/gnoll/c_includes/
	rm -rf src/python/code/gnoll.egg-info/

	cp -r build/  src/python/code/gnoll/c_build/
	cp -r src/grammar/  src/python/code/gnoll/c_includes/

	cd src/python/ ; python3 -m build
	echo "------------------INSTALL------------------------"
	python3 -m pip install -vvv --user --no-index --find-links=src/python/dist/ --force-reinstall --ignore-installed gnoll
	echo "-------------------- TEST ----------------------"
	python3 -c "from gnoll import parser as dt; dt.roll('2')"


.PHONY: publish
publish: test
	#twine upload --repository-url https://test.pypi.org/legacy/ src/python/dist/*
	twine upload src/python/dist/*

# An example
.PHONY: swig
swig: swig_perl swig_java swig_go swig_js

.PHONY: swig_go
swig_go:
	mkdir -p build/go/
	swig -go -outdir build/go -o src/go/gnoll_wrap.c src/swig/GNOLL.i

.PHONY: swig_java
swig_java:
	mkdir -p build/java/
	swig -java -outdir build/java -o src/java/gnoll_wrap.c src/swig/GNOLL.i

.PHONY: swig_js
swig_js:
	mkdir -p build/js/
	swig -javascript -outdir build/js -o src/js/gnoll_wrap.c src/swig/GNOLL.i


# ========= PHP =========
# Note: SWIG only supports PHP 5.0 - 5.3 which is very outdated
# Current version at time of writing is 8.0

# ========= PERL =========
.PHONY: swig_perl compile_perl perl
swig_perl: clean yacc lex
	mkdir -p build/perl/
	swig -perl -outdir build/perl -o build/perl/gnoll_wrap.c src/swig/GNOLL.i

compile_perl: swig_perl
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

# Perl
	cc -fPIC -c build/perl/gnoll_wrap.c -I/usr/lib/x86_64-linux-gnu/perl/5.30/CORE/ -Dbool=char -Doff64_t=__off64_t -o build/gnoll_perl_wrap.o

	cc -shared -o build/gnoll.so build/gnoll_perl_wrap.o build/die.o build/macro.o build/tab.o build/cc.o build/lex.o build/vec.o build/rso.o

perl: compile_perl
	echo "Done"
	cp build/perl/gnoll.pm src/perl/gnoll.pm
	cp build/gnoll.so src/perl/gnoll.so
	perl src/perl/example_application.pl

.PHONY: go
go: clean yacc lex compile
	cp build/dice.so build/libdice.so 
	cd src/go && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  go build main.go && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  go run main.go && cd ../..

