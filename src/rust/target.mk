.PHONY: rust

rust: all
	echo "pwd is $(shell pwd)"
	ls "$(shell pwd)/build/"
	$(eval LD_LIBRARY_PATH := $(shell pwd)/build/)
	echo "ldpath is $(LD_LIBRARY_PATH)"
	ls "$(shell pwd)/build/libdice.so" -las
	ls "$(LD_LIBRARY_PATH)/libdice.so" -las
	ld -ldice
	ldd "$(shell pwd)/build/libdice.so"
	cd src/rust && cargo build -v
	cd src/rust && cargo run 
