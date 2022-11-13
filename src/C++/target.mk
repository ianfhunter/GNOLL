CXX?=g++
cpp:
	$(CXX) src/C++/main.cpp -I src/grammar/ -ldice -Lbuild/
