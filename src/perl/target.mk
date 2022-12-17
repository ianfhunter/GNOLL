.PHONY: swig_perl compile_perl perl clean_perl

swig_perl: clean yacc lex compile $(OBJECTS)
	mkdir -p build/perl/
	swig -perl -outdir build/perl -o build/perl/gnoll_wrap.c src/swig/GNOLL.i

PERL_VERSION=5.30
compile_perl: swig_perl 
	$(CC) -fPIC -c build/perl/gnoll_wrap.c -I/usr/lib/x86_64-linux-gnu/perl/$(PERL_VERSION)/CORE/ -Dbool=char -Doff64_t=__off64_t -o build/gnoll_perl_wrap.o
	$(CC) -shared -o build/gnoll.so build/gnoll_perl_wrap.o $(OBJECTS)

perl: compile_perl
	echo "Done"
	cp build/perl/gnoll.pm src/perl/gnoll.pm
	cp build/gnoll.so src/perl/gnoll.so
	perl src/perl/example_application.pl

perl_clean: 
	rm MYMETA.json | true
	rm MYMETA.yml | true
	rm result.die | true
