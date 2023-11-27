.PHONY: rust

rust: all
	export LD_LIBRARY_PATH=$(shell pwd)/build/
	export LIBRARY_PATH=$LD_LIBRARY_PATH
	sudo cp $(shell pwd)/build/libdice.so /usr/local/lib/libdice.so
	cd src/rust && cargo build 
	cd src/rust && LD_LIBRARY_PATH=$(shell pwd)/build/ cargo run --verbose 
