.PHONY: r

r: clean yacc lex compile $(OBJECTS)
	$(CC) -shared -o build/r/dice.so $(OBJECTS) $(ARC4RANDOM) -lR
	Rscript src/R/main.r
