.PHONY: rust

rust: all
	echo $LD_LIBRARY_PATH
	echo $PWD
	ls $(PWD)/build/libdice.so
	ld -ldice
	cd src/rust && ldd $(PWD)/build/libdice.so
	cd src/rust && cargo build -v
	cd src/rust && cargo run 
