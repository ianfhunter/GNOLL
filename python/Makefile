
all:

lint:
	autopep8 dice_tower/test.py > tmp
	cat tmp > dice_tower/test.py
	autopep8 dice_tower/dice.py > tmp
	cat tmp > dice_tower/dice.py
	autopep8 dice_tower/utils.py > tmp
	cat tmp > dice_tower/utils.py
	rm tmp

	python3 -m pyflakes dice_tower/test.py
	python3 -m pycodestyle dice_tower/test.py

	python3 -m pyflakes dice_tower/dice.py
	python3 -m pycodestyle dice_tower/dice.py

	python3 -m pyflakes dice_tower/utils.py
	python3 -m pycodestyle dice_tower/utils.py


coverage:
	coverage run dice_tower/test.py
	coverage report

test:
	python3 dice_tower/test.py

release_package:
	# Increment version
	-sudo rm dice_tower/dist -r
	sudo python3 setup.py develop sdist bdist_wheel
	http_proxy="" https_proxy="" python3 -m twine upload dist/*

test_package:
	#increment version
	-sudo rm dice_tower/dist -r
	sudo python3 setup.py develop sdist bdist_wheel
	pip3 uninstall dice-tower
	pip3 install dist/dice_tower-1.2.13.tar.gz --user