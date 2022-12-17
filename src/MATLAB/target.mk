.PHONY: matlab
matlab: all
	octave src/MATLAB/main.m build/libdice.so
