.PHONY: rust

rust: all
	cd src/rust && cargo build
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ rustc -C debuginfo=2 -L $(PWD)/../../build/ -l dice gnoll_bindings.rs
	cd src/rust && ./gnoll_bindings
