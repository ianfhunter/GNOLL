
.PHONY: fortran
fortran: all
	cp build/dice.so build/libdice.so 
	cd src/FORTRAN && ln -s ../../build c_build
	cd src/FORTRAN && ln -s ../../src/grammar c_includes
	cd src/FORTRAN && LD_LIBRARY_PATH="${PWD}/build:${LD_LIBRARY_PATH}"  gfortran -o main gnoll.f90 -lroll_and_write && ls output.die
