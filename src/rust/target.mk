.PHONY: rust

rust: all
	cd src/rust && cargo build
        export LD_LIBRARY_PATH=$(PWD)/build/
	cd src/rust && rustc -l dice static=dice gnoll_bindings.rs
	cd src/rust && ./gnoll_bindings
