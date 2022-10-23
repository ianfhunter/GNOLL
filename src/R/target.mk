.PHONY: r

r: clean yacc lex
	Rscript src/R/main.r
