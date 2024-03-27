.PHONY: r

r: clean yacc lex compile $(OBJECTS)
	mkdir -p build/r/
	$(CC) -shared -o build/r/dice.so $(OBJECTS) $(ARC4RANDOM) -lR  -lpcg_random -L$(PCG_SRC) 
	Rscript src/R/main.r
