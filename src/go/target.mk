
.PHONY: go
go: all
	cp build/dice.so build/libdice.so 
	cd src/go && ln -s ../../build c_build
	cd src/go && ln -s ../../src/grammar c_includes
	cd src/go && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  go build main.go && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  go run main.go && cd ../..
