
.PHONY: javascript
javascript:
	emcc -O3 build/y.tab.c \
        src/grammar/rolls/sided_dice.c \
        src/grammar/rolls/condition_checking.c \
        src/grammar/vector_functions.c \
        src/grammar/dice_logic.c \
        src/grammar/macro_logic.c \
        src/grammar/safe_functions.c \
        build/lex.yy.c \
        -Isrc/grammar/	

js: javascript  
# Make alias for ease of use
	@echo > /dev/null
