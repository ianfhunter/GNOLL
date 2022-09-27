
.PHONY: pip publish python_clean
pip : all
	echo "----------------- BUILD -------------------------"
	# Copy Build
	rm -rf code/gnoll/c_build/
	rm -rf code/gnoll/c_includes/
	rm -rf code/gnoll.egg-info/

	cp -r ../../build/  code/gnoll/c_build/
	cp -r ../grammar/  code/gnoll/c_includes/

	python3 -m build
	echo "------------------INSTALL------------------------"
	python3 -m pip install -vvv --user --find-links=dist/ --force-reinstall --ignore-installed gnoll
	echo "-------------------- TEST ----------------------"
	python3 -c "from gnoll import parser as dt; dt.roll('2')"

publish: test
	#twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	twine upload dist/*

python_clean: 
# Python Packaging can create extraoneous files
	rm src/ | true
	rm dist/ | true
	rm build/ | true
	rm LICENSE | true
	rm Makefile | true
