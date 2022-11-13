CODEDIRS=./src/grammar ./src/grammar/rolls ./src/grammar/util ./src/grammar/operations ./src/grammar/external  
INCDIRS=./src/grammar

CC=cc

ifeq ($(CC),g++)
   STANDARD= -std=c++11
else ifeq ($(CC),clang++)
   STANDARD= -std=c++11
else
   STANDARD= -std=c99
endif

OPT=-O3 $(STANDARD) -Wall -Wextra -Werror -pedantic -Wcast-align \
	-Wcast-qual -Wdisabled-optimization -Winit-self \
	-Wmissing-declarations -Wmissing-include-dirs \
	-Wredundant-decls -Wshadow -Wsign-conversion \
	-Wundef -Wno-unused -Wformat=2

# -ffast-math # Problematic for Python 

# YACC/LEX fails for the following, so disabled:
# -Wswitch-default  -Wstrict-overflow=5

# EMCC fails for the following, so disabled:
# -Wlogical-op

# === DEBUG OPTIONS ====
DEBUG=0
ifeq ($(DEBUG), 1)
OPT=-O0 -g  # Valgrind info
PARSER_DEBUG:=--debug --verbose
else
PARSER_DEBUG:=
endif

USE_SECURE_RANDOM=0
ifeq ($(USE_SECURE_RANDOM), 1)
#$(shell echo "Using Fast, but Cryptographically insecure random fn")
ARC4RANDOM:=-lbsd `pkg-config --libs libbsd`
else
#$(shell echo abc) "Using Cryptographically Secure, but slow random fn")
ARC4RANDOM:=
endif

YACC_FALLBACK=0
ifeq ($(YACC_FALLBACK), 1)
#$(shell echo USING YACC)
PARSER:=yacc
else
#$(shell echo USING BISON)
PARSER:=bison --yacc
endif

LEX_FALLBACK=0
ifeq ($(LEX_FALLBACK), 1)
#$(shell echo USING LEX)
LEXER:=lex
else
#$(shell echo USING FLEX)
LEXER:=flex -f -Ca -Ce -Cr 
endif

# add flags and the include paths
DEFS=-DUSE_SECURE_RANDOM=${USE_SECURE_RANDOM} -DJUST_YACC=${YACC_FALLBACK} -DBREAKDOWN

CFLAGS=$(foreach D,$(INCDIRS),-I$(D)) $(OPT) $(DEFS)

# add flags to build for shared library and add include paths
SHAREDCFLAGS=-fPIC -c $(foreach D,$(INCDIRS),-I$(D)) $(ARC4RANDOM) $(DEFS)

# generate list of c files and remove y.tab.c from src/grammar directory
CFILES=$(foreach D,$(CODEDIRS),$(wildcard $(D)/*.c)) build/lex.yy.c build/y.tab.c
CFILES:=$(filter-out ./src/grammar/y.tab.c, $(CFILES))

# Create object files from the above c files.
OBJECTS=$(patsubst %.c,%.o,$(CFILES))
# To be under build/* as in grammar/*
OBJECTS:=$(subst ./src/grammar/,,$(OBJECTS))
OBJECTS:=$(addprefix build/,$(OBJECTS))
# Exception: Lex/Yacc generated files
OBJECTS:=$(subst build/build/,build/,$(OBJECTS))

# TODO: Would be nice to automatically get these.
CFILE_SUBDIRS=rolls util operations external

all: clean yacc lex compile shared
	echo "== Build Complete =="

yacc:
	mkdir -p build
	$(foreach BD,$(CFILE_SUBDIRS),mkdir -p build/$(BD))
	$(PARSER) -d src/grammar/dice.yacc $(PARSER_DEBUG) 
	mv y.tab.c build/y.tab.c
	mv y.tab.h build/y.tab.h
	mv y.output build/y.output | true	# Only present with verbose
lex:
	$(LEXER) src/grammar/dice.lex
	mv lex.yy.c build/lex.yy.c

# Executable
compile:
	# FLEX creates warning when run with -f
        # MacOS creates warnings for signs.
	$(CC) $(CFLAGS) $(CFILES) $(ARC4RANDOM) \
           -Wno-error=implicit-function-declaration \
           -Wno-sign-conversion -Wno-sign-compare

# Shared Lib
shared: $(OBJECTS)
	$(CC) -shared -o build/dice.so $^ $(ARC4RANDOM)

# Linux
	mv ./a.out build/dice | true
# Windows
	mv ./a.exe build/dice | true

# hardcode for lex and yacc files
build/y.tab.o: 
	$(CC) $(SHAREDCFLAGS) -c build/y.tab.c -o $@
build/lex.yy.o:
	$(CC) $(SHAREDCFLAGS) -c build/lex.yy.c -o $@  

# Wildcard everything else
build/*/%.o:src/grammar/*/%.c
	$(CC) $(SHAREDCFLAGS) -c  $^ -o $@
build/%.o:src/grammar/%.c
	$(CC) $(SHAREDCFLAGS) -c -o $@ $^

test_no_pip : python
	python3 -m pytest tests/python/ -xs

test : pip
	python3 -m pytest tests/python/ -xs

include src/*/target.mk

clean: perl_clean python_clean clean_js
	rm -rf build
	rm src/grammar/test_dice.yacc | true
