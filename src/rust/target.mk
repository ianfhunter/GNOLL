.PHONY: rust

rust: all
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ cargo build -v
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ cargo run 
