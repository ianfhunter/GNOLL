.PHONY: rust

rust: all
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ cargo build
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ rustc -C debuginfo=2 -L $(PWD)/../../build/ -ldice gnoll_bindings.rs
	cd src/rust && ./gnoll_bindings
