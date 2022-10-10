

JS_OPT=-O3 -Wall

.PHONY: javascript
javascript:
	emcc $(JS_OPT) $(CFILES) \
	$(SHAREDCFLAGS)

js: javascript  
# Make alias for ease of use
	@echo > /dev/null
