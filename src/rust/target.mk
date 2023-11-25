.PHONY: rust

rust: all
	echo "ONE:" && echo $LD_LIBRARY_PATH
	echo "TWO;" && ls $(PWD)/build/libdice.so
	echo ld -ldice
	cd src/rust && ldd $(PWD)/build/libdice.so
	cd src/rust && cargo build -v
	cd src/rust && cargo run 
