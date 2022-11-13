CXX?=g++
cpp:
    $(CXX) src/cpp/main.cpp -I src/grammar/shared_header.h -ldice -Lbuild/
