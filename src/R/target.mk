.PHONY: r

r: clean yacc lex compile
	$(CC) -shared -o build/r/dice.so $(OBJECTS) $(ARC4RANDOM) -lR
	Rscript src/R/main.r
