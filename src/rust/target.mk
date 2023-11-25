.PHONY: rust

rust: all
	echo "LDPATH"
	export LD_LIBRARY_PATH=$(PWD)/build/:$LD_LIBRARY_PATH
	echo ${LD_LIBRARY_PATH}
	ls $(PWD)/build/libdice.so -las
	ld -ldice
	ldd $(PWD)/build/libdice.so
	cd src/rust && cargo build -v
	cd src/rust && cargo run 
