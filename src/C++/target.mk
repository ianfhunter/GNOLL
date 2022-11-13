CXX?=g++
cpp: all
	$(CXX) src/C++/main.cpp -I src/grammar/ -ldice -Lbuild/
	LD_LIBRARY_PATH=$(PWD)/build/ ./a.out
