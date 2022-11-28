
.PHONY: haskell
haskell: clean shared
	sudo cp build/dice.so /usr/lib/dice.so 
	cd src/haskell/ && cabal build
