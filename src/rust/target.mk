.PHONY: rust

rust: all
	echo "LDPATH"
	echo "pwd is $(shell pwd)"
	ls "$(shell pwd)/build/"
	export LD_LIBRARY_PATH="$(shell pwd)/build/":"$LD_LIBRARY_PATH*
	echo "$LD_LIBRARY_PATH"
	ls "$(shell pwd)/build/libdice.so" -las
	ld -ldice
	ldd "$(shell pwd)/build/libdice.so"
	cd src/rust && cargo build -v
	cd src/rust && cargo run 
