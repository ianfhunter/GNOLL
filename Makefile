clean:
	-rm grammar/* -r
	#alias antlr4

python:
	cd external ; make download ; cd ..
	bash ./setup_antlr.sh 4.7.2 Python3
	antlr4 dice.g4 -o python/dice_tower/grammar -Dlanguage=Python3
	cd python ; make all ; cd ..

javascript: clean
	cd external ; make download ; cd ..
	# TODO - : on linux, ; on windows.
	bash ./setup_antlr.sh 4.7.2 Javascript
	npm install antlr4
	cd javascript ; make all ; cd ..

all : python
	echo ""

test : all
	cd python ; make test ; cd ..

lint :
	cd python ; make lint ; cd ..

install :
	cd external/antlr4/ ; export MAVEN_OPTS="-Xmx1G" ; mvn clean
	cd external/antlr4/ ; export MAVEN_OPTS="-Xmx1G" ; mvn -DskipTests install
	cd external/antlr4/ ; export MAVEN_OPTS="-Xmx1G" ; mvn package

.PHONY: clean python javascript all