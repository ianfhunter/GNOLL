.PHONY: rust

rust: all
	cd src/rust && cargo build
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ rustc -l dice gnoll_bindings.rs
	cd src/rust && ./gnoll_bindings
