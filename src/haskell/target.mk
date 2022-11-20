
.PHONY: haskell
haskell: clean yacc lex compile shared
	sudo cp build/dice.so /usr/lib/dice.so 
	cd src/haskell/ && cabal build
