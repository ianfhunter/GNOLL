.PHONY: java

java_binding:
	cd src/java/ ; javac org/gnoll/DiceNotationParser.java  -h .; cd ../..
	

# https://stackoverflow.com/questions/14529720/how-to-make-jni-h-be-found#comment123062499_55191414
JAVA_HOME=$(shell dirname $$(readlink -f $$(which java))|sed 's/bin//')

java: clean yacc lex compile $(OBJECTS)
	mkdir -p build/java/
	$(CC) $(SHAREDCFLAGS) -c src/java/org_gnoll_DiceNotationParser.c -I $(JAVA_HOME)/include -I $(JAVA_HOME)/include/linux
	$(CC) -shared -o build/java/libdice.so $(OBJECTS) $(ARC4RANDOM) -Wl,-soname,gnoll
	cp build/java/libdice.so  src/java/libdice.so
	cd src/java; LD_LIBRARY_PATH=build/java/ javac -cp ".:$(PWD)/src/java/" test.java
        cd src/java; LD_LIBRARY_PATH=build/java/ java -cp ".:$(PWD)/src/java/" Test #test.java
