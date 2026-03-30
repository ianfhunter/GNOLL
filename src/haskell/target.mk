
.PHONY: haskell
# Absolute rpath so the linked binary finds libdice.so without LD_LIBRARY_PATH at run time.
HASKELL_DICE_LIB_DIR := $(abspath src/haskell/lib)

haskell: all
	mkdir -p src/haskell/lib
	cp build/libdice.so src/haskell/lib/libdice.so
	cd src/haskell/ && \
	  LD_LIBRARY_PATH="$(HASKELL_DICE_LIB_DIR):$$LD_LIBRARY_PATH" \
	  cabal build \
	    --ghc-options="-optl-Wl,-rpath,$(HASKELL_DICE_LIB_DIR)"
