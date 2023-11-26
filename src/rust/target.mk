.PHONY: rust

rust: all
	echo "pwd is $(shell pwd)"
	ls "$(shell pwd)/build/"
	echo "explicit"
	ld -L"$(shell pwd)/build/" -ldice
	export LD_LIBRARY_PATH=$(shell pwd)/build/
	export LIBRARY_PATH=LD_LIBRARY_PATH
	cd src/rust && cargo build 
	cd src/rust && cargo run 
