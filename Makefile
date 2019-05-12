
# apt install antlr4
# pip install antlr4-python3-runtime==ANTLRVERSION

all:
	-rm grammar/* -r
	antlr4 dice.g4 -o grammar -Dlanguage=Python3

lint:
	autopep8 test.py > tmp
	cat tmp > test.py
	autopep8 dice.py > tmp
	cat tmp > dice.py
	rm tmp

	python3 -m pyflakes test.py
	python3 -m pycodestyle test.py

	python3 -m pyflakes dice.py
	python3 -m pycodestyle dice.py

coverage:
	coverage run test.py
	coverage report

test: all
	python3 test.py