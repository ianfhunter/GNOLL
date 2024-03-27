.PHONY: pip publish python_clean python 
python: all
	echo "----------------- BUILD -------------------------"
	# Copy Build
	rm -rf src/python/code/gnoll/c_build/
	rm -rf src/python/code/gnoll/c_includes/
	rm -rf src/python/code/gnoll.egg-info/

	cp -r build/  src/python/code/gnoll/c_build/
	rsync -avhR --mkpath --progress src/grammar/ src/python/code/gnoll/c_includes/ \
               --exclude creating gnoll-4.4.0/code/gnoll/c_includes/external/pcg-c/extras \
               --exclude creating gnoll-4.4.0/code/gnoll/c_includes/external/pcg-c/sample \
               --exclude creating gnoll-4.4.0/code/gnoll/c_includes/external/pcg-c/test-high \
               --exclude creating gnoll-4.4.0/code/gnoll/c_includes/external/pcg-c/test-low

pip : python
	cd src/python/ ; python3 -m build
	python3 -m pip install -vvv --user --find-links=src/python/dist/ --force-reinstall --ignore-installed src/python/
	python3 -c "from gnoll import roll; roll('2')"

publish: test
	#twine upload --repository-url https://test.pypi.org/legacy/ src/python/dist/*
	twine upload src/python/dist/*

python_clean: 
# Python Packaging can create extraoneous files
	rm src/python/src/ | true
	rm src/python/dist/ | true
	rm src/python/build/ | true
	rm src/python/LICENSE | true
	rm src/python/Makefile | true
