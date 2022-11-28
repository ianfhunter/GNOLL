
.PHONY: go
go: clean shared
	cp build/dice.so build/libdice.so 
	cd src/go && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  go build main.go && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  go run main.go && cd ../..
