.PHONY: cs
cs: all
	csc src/CSharp/main.cs
	LD_LIBRARY_PATH=$(PWD)/build/ mono main.exe
