.PHONY: r

r: clean yacc lex compile $(OBJECTS)
	mkdir -p build/r/
	$(CC) -shared -o build/r/dice.so $(OBJECTS) $(ARC4RANDOM) -lR
	Rscript src/R/main.r
