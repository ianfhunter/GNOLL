
# apt install antlr4
# pip install antlr4-python3-runtime==ANTLRVERSION

all:
	-rm grammar/* -r
	antlr4 dice.g4 -o grammar -Dlanguage=Python3

lint: 
	python3 -m pyflakes test.py

test: all
	python3 test.py