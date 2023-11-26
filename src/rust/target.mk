.PHONY: rust

rust: all
	echo "pwd is $(shell pwd)"
	ls "$(shell pwd)/build/"
	echo "explicit"
	ld -L"$(shell pwd)/build/" -ldice
	export LD_LIBRARY_PATH=$(shell pwd)/build/ && ld -ldice
	echo "done"
	$(eval LD_LIBRARY_PATH := $(shell pwd)/build/)
	export LD_LIBRARY_PATH
	echo "ldpath is $(LD_LIBRARY_PATH)"
	ls "$(shell pwd)/build/libdice.so" -las
	ls "$(LD_LIBRARY_PATH)/libdice.so" -las
	ld -ldice
	ldd "$(shell pwd)/build/libdice.so"
	cd src/rust && cargo build -v
	cd src/rust && cargo run 
