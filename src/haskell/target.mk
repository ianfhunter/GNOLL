
.PHONY: haskell
haskell: all
	mkdir -p src/haskell/lib
	cp build/libdice.so src/haskell/lib/libdice.so
	cd src/haskell/ && cabal build
