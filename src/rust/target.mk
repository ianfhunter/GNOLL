.PHONY: rust

rust: all
	cp build/dice.so build/libdice.so 
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ cargo build -v
	cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ cargo run 
	# cd src/rust && LD_LIBRARY_PATH=$(PWD)/../../build/ rustc -C debuginfo=2 -L $(PWD)/../../build/ -ldice gnoll_bindings.rs
	# cd src/rust && ./gnoll_bindings
