.PHONY: rust

rust: all
	echo "LDPATH"
	echo "pwd is $(pwd)"
	ls "$(pwd)/build/"
	export LD_LIBRARY_PATH="$(pwd)/build/":"$LD_LIBRARY_PATH*
	echo "$LD_LIBRARY_PATH"
	ls "$(pwd)/build/libdice.so" -las
	ld -ldice
	ldd "$(pwd)/build/libdice.so"
	cd src/rust && cargo build -v
	cd src/rust && cargo run 
