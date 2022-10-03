---
title: Technical Setup
published: true
nav_order: 0
---

# Technical Setup
## OS Information

- Linux - Tested on Ubuntu '18.
- Windows - Tested on Windows Subsystem for Linux (WSL)
- Mac - Untested.

## Common Pre-requisites
```bash
sudo apt-get install bison flex make python3-pip -y
```

## C/C++
```
make all
```

## Go
```
make go
```

## Python
Available from [PyPi](https://pypi.org/project/gnoll/)
```
pip install gnoll
```
If you are running from sourcecode:
```
make python
```

## Perl
```
make perl
```

## Javascript Setup

### Pre-Requisites
```bash
sudo apt-get install emscripten nodejs
```

### Build
```
make javascript
```

### Run
```
node a.out.js
```

## Something Else?
### SWIG
The swig bindings are already generated for you in `src/swig/gnoll.i`. Follow the specific instructions in the SWIG documentation to build your own binding.
Note: The current bindings do not return a result directly - You should read from the file that is generated.

### Shared Library
Many languages allow importing of code via shared object. You can find this .o file in the build folder after running `make all`
