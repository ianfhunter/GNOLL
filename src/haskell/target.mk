
.PHONY: haskell
haskell: clean yacc lex compile
	cp build/dice.so src/haskell/dice.so 
	cd src/haskell/ && cabal build