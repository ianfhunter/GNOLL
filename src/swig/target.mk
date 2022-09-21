
.PHONY: swig
swig: swig_perl swig_java swig_go swig_js

.PHONY: swig_go
swig_go:
	mkdir -p build/go/
	swig -go -outdir build/go -o src/go/gnoll_wrap.c src/swig/GNOLL.i

.PHONY: swig_java
swig_java:
	mkdir -p build/java/
	swig -java -outdir build/java -o src/java/gnoll_wrap.c src/swig/GNOLL.i

.PHONY: swig_js
swig_js:
	mkdir -p build/js/
	swig -javascript -outdir build/js -o src/js/gnoll_wrap.c src/swig/GNOLL.i

