

JS_OPT=-O3 -Wall
.PHONY: javascript
javascript: clean yacc lex
	mkdir -p build/js/
	emcc $(JS_OPT) $(CFILES) \
	$(CFLAGS) \
        -o build/js/a.out.js -Wno-error=implicit-function-declaration

js: javascript  
# Make alias for ease of use
	@echo > /dev/null

clean_js:
	rm -rf build/js
