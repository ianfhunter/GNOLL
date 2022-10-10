

JS_OPT=-O3 -Wall
.PHONY: javascript
javascript:
	mkdir -p build/js/
	emcc $(JS_OPT) $(CFILES) \
	$(CFLAGS) \
        -o build/js/a.out.js

js: javascript  
# Make alias for ease of use
	@echo > /dev/null
