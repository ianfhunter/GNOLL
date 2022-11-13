CXX?=g++
cpp:
	$(CXX) src/C++/main.cpp -I src/grammar/shared_header.h -ldice -Lbuild/
