
.PHONY: haskell
# Absolute rpath so the linked binary finds libdice.so. cabal.project.local is required
# because `cabal run` may relink without Makefile's --ghc-options (e.g. "Flags changed").
HASKELL_DICE_LIB_DIR := $(abspath src/haskell/lib)

haskell: all
	mkdir -p src/haskell/lib
	cp build/libdice.so src/haskell/lib/libdice.so
	printf 'package src\n  ghc-options: -optl-Wl,-rpath,$(HASKELL_DICE_LIB_DIR)\n' > src/haskell/cabal.project.local
	cd src/haskell/ && \
	  LD_LIBRARY_PATH="$(HASKELL_DICE_LIB_DIR):$$LD_LIBRARY_PATH" \
	  cabal build
