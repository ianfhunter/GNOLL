.PHONY: rust

rust: all
	echo "pwd is $(shell pwd)"
	ls "$(shell pwd)/build/"
	echo "explicit"
	ld -L"$(shell pwd)/build/" -ldice
	export LD_LIBRARY_PATH=$(shell pwd)/build/
	cd src/rust && RUSTFLAGS="-C link-arg=-L$(shell pwd)/build/" cargo build 
	cd src/rust && cargo run 
