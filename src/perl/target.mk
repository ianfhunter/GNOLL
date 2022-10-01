.PHONY: swig_perl compile_perl perl clean_perl

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

perl_clean: 
	rm MYMETA.json | true
	rm MYMETA.yml | true
	rm result.die | true