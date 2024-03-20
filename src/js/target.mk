
JS_OPT=-O3 -Wall

# YACC/LEX generates code with errors, so disabling warning-to-error escalation
DISABLE_ERRORS= -Wno-error=implicit-function-declaration

ifneq ($(OS),Windows_NT)
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
DISABLE_ERRORS+= -Wno-error  #  -Wno-error=sign-conversion -Wno-error=sign-compare
endif
endif


.PHONY: javascript
javascript: clean yacc lex
	mkdir -p build/js/
	emcc $(JS_OPT) $(CFILES) \
	$(CFLAGS) \
	-o build/js/a.out.js $(DISABLE_ERRORS) -D__EMSCRIPTEN__

js: javascript  
# Make alias for ease of use
	@echo > /dev/null

clean_js:
	rm -rf build/js

jsweb: clean yacc lex
	mkdir -p build/jsweb
	emcc \
	$(CFILES) \
	-I ./src/grammar \
	-o src/js/gnollwasm.js \
	-D__EMSCRIPTEN__ \
	-s MODULARIZE=1 \
	-s EXPORT_ES6=1 \
	--pre-js ./src/js/preface.js \
	-s WASM=1 -s EXPORTED_RUNTIME_METHODS='["cwrap", "print"]' \
	-s EXPORTED_FUNCTIONS="['_roll_full_options']"

jsbundle: jsweb
	cp src/js/*.html src/js/*.wasm ./build/jsweb/
	yarn --cwd ./src/js run webpack-cli b
