.PHONY: r

r: clean yacc lex compile shared
	$(CC) -shared -o build/r/dice.so $^ $(ARC4RANDOM) -lR
	Rscript src/R/main.r
