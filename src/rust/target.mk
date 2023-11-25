.PHONY: rust

rust: all
	nm build/libdice.so
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/:/home/runner/work/GNOLL/GNOLL/build/ cargo build -v
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/:/home/runner/work/GNOLL/GNOLL/build/ cargo run 
