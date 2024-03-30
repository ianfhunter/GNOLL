
JS_OPT=-O3 -Wall

# YACC/LEX generates code with errors, so disabling warning-to-error escalation
# PCG also generates code with errors
DISABLE_ERRORS= -Wno-error=implicit-function-declaration -Wno-sign-conversion -Wno-sign-compare -Wno-implicit-int-conversion -Wno-undef -Wno-shorten-64-to-32 

ifneq ($(OS),Windows_NT)
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
DISABLE_ERRORS+= -Wno-error  #  -Wno-error=sign-conversion -Wno-error=sign-compare
endif
endif


.PHONY: javascript
javascript: clean yacc lex jspcg
	mkdir -p build/js/
	emcc $(JS_OPT) $(CFILES) \
	$(CFLAGS) \
	-o build/js/a.out.js $(DISABLE_ERRORS) -D__EMSCRIPTEN__

js: javascript  
# Make alias for ease of use
	@echo > /dev/null

clean_js:
	rm -rf build/js

jsweb: clean yacc lex jspcg
	mkdir -p build/jsweb
	emcc \
	$(CFILES) \
	-I ./src/grammar \
        -I ./src/grammar/external/pcg-c/include/ \
	-o src/js/gnollwasm.js \
	-D__EMSCRIPTEN__ \
	-s MODULARIZE=1 \
	-sSINGLE_FILE \
	-s EXPORT_NAME=gnollwasm \
	--pre-js ./src/js/preface.js \
	-s WASM=1 -s EXPORTED_RUNTIME_METHODS='["cwrap", "ccall", "print"]' \
	-s EXPORTED_FUNCTIONS="['_roll_full_options']"

#-s EXPORT_ES6=1 \

jsbundle: jsweb
	#cp src/js/*.html src/js/*.wasm ./build/jsweb/
	cp src/js/*.html ./build/jsweb/
	yarn --cwd ./src/js run webpack-cli b

jspcg:
	emcc src/grammar/external/pcg-c/src/pcg-rngs-64.c ../include/pcg_variants.h 
	
