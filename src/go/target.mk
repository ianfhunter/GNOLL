
.PHONY: go
go: all
	cp build/dice.so build/libdice.so 
	ln -s build src/go/c_build/
	ln -s src/grammar/ src/go/c_includes
	cd src/go && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  go build main.go && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  go run main.go && cd ../..
