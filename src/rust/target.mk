.PHONY: rust

rust: all
	echo "ONE:" && ls $(PWD)/build/
	echo "TWO;" && ls $(PWD)/build/libdice.so
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ ldd $(PWD)/../../build/libdice.so
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ cargo build -v
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ cargo run 
