
all:

lint:
	autopep8 test.py > tmp
	cat tmp > test.py
	autopep8 dice.py > tmp
	cat tmp > dice.py
	autopep8 utils.py > tmp
	cat tmp > utils.py
	rm tmp

	python3 -m pyflakes test.py
	python3 -m pycodestyle test.py

	python3 -m pyflakes dice.py
	python3 -m pycodestyle dice.py

	python3 -m pyflakes utils.py
	python3 -m pycodestyle utils.py


coverage:
	coverage run test.py
	coverage report

test:
	python3 test.py
