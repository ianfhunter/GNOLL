clean:
	-rm grammar/* -r

python:
	antlr4 dice.g4 -o python/grammar -Dlanguage=Python3
	cd python ; make all ; cd ..

javascript:
	antlr4 dice.g4 -o javascript/grammar -Dlanguage=Javascript
	cd javascript ; make all ; cd ..

all : python
	echo ""

test : all
	cd python ; make test ; cd ..

lint :
	cd python ; make lint ; cd ..


.PHONY: clean python javascript