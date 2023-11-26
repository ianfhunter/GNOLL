.PHONY: rust

rust: all
	echo "pwd is $(shell pwd)"
	ls "$(shell pwd)/build/"
	echo "explicit"
	ld -L"$(shell pwd)/build/" -ldice
	export LD_LIBRARY_PATH=$(shell pwd)/build/
	export LIBRARY_PATH=$LD_LIBRARY_PATH
	sudo cp $(shell pwd)/build/libdice.so /usr/local/lib/libdice.so
	echo "BUILD"
	cd src/rust && cargo build 
	echo "RUN"
	cd src/rust && cargo run 
