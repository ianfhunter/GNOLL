.PHONY: java

java_binding:
	

# https://stackoverflow.com/questions/14529720/how-to-make-jni-h-be-found#comment123062499_55191414
JAVA_HOME=$(shell dirname $$(readlink -f $$(which java))|sed 's/bin//')
JAVA_FOLDER=$(PWD)/src/java

java: clean yacc lex compile $(OBJECTS)
	mkdir -p build/java/
	cd $(JAVA_FOLDER)/src ; javac org/gnoll/DiceNotationParser.java  -h .; cd ../..
	$(CC) $(SHAREDCFLAGS) -c src/java/src/org_gnoll_DiceNotationParser.c -I $(JAVA_HOME)/include -I $(JAVA_HOME)/include/linux
	$(CC) -shared -o build/java/libdice.so org_gnoll_DiceNotationParser.o $(OBJECTS) $(ARC4RANDOM) -Wl,-soname,gnoll
	cp build/java/libdice.so  src/java/libdice.so
	cd $(JAVA_FOLDER)/src/; LD_LIBRARY_PATH=$(PWD)/build/java/ javac -cp .:$(JAVA_FOLDER)/classes/ -d $(JAVA_FOLDER)/classes/ Test.java
	cd $(JAVA_FOLDER)/src/; LD_LIBRARY_PATH=$(PWD)/build/java/ java -cp .:$(JAVA_FOLDER)/classes/ Test
