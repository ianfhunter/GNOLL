.PHONY: rust

rust: all
	cd src/rust && cargo build
	cd src/rust && rustc -l../build static=dice gnoll_bindings.rs
	cd src/rust && ./gnoll_bindings
