---
title: Setup
parent: Technical Information
published: true
nav_order: 0
---

# Setup
## OS Information

| OS | Version | Tested (From Source) | Tested (PyPi) |
| -- | ------- | -------------------- | ------------- |
| Linux | Ubuntu 18.04 | Yes | Yes |
| Windows | WSL1 | Yes | Yes |
| Windows | Win11 | No | No |
| MacOS | 12 | Yes | Yes |

## Common Pre-requisites
```bash
sudo apt-get install bison flex make python3-pip -y
```

## Language Bindings 

We have tested several language bindings to GNOLL. 
The intention is not to be exhaustively compatible with every version, but a useful reference to help you set up GNOLL for your own software.

### C
This is the default build target.
Tested with GCC and Clang Compilers and is C99 compliant.

```bash
make all
./a.out "1d20
```

### C++
Tested with Clang Compiler, Ubuntu 22.04

```bash
make cpp
```

### CSharp
Tested with Mono Compiler, Ubuntu 22.04
```bash
make cs
```

### Go
Tested with Golang 1.18, Ubuntu 22.04
```bash
make go
```

### Haskell
Tested with ghc 9.4.3, cabal 3.0.0.0-3build1.1, Ubuntu 22.04
```
make haskell
```

### Python
Available from [PyPi](https://pypi.org/project/gnoll/)
Tested with Python3.10, Ubuntu 22.04
```bash
pip install gnoll
```
If you are running from sourcecode:
```bash
make python
```

### Perl
Tested on Perl 5.30, Ubuntu 20.04
```bash
make perl
```
To make for another version, $PERL_VERSION must be set (default: 5.30)

### Java
Tested with openjdk-8, Ubuntu 22.04
```bash
make java
```

### Julia
Tested on Ubuntu 20.04, Julia 1.4.1

Available from [JuliaHub](https://juliahub.com/ui/Packages/GnollDiceNotation/WetJc/)
```
make julia
```

### JavaScript Setup

Tested as an executable, untested in the browser.

Tested with emscripten 3.1.6, Ubuntu 22.04

#### Pre-Requisites
```bash
sudo apt-get install emscripten nodejs
```

##### Build
```bash
make javascript
```

##### Run
```bash
node a.out.js
```

### PHP
Tested on PHP 8.1.13, Ubuntu 22.04
```bash
make php
```

### R
Tested on R 4.2.2, Ubuntu 22.04
```bash
make r
```

### Ruby
Tetsed on Ruby 3.0, Ubuntu 22.04
```bash
make ruby
```

## Something Else?
### SWIG
The swig bindings are already generated for you in `src/swig/gnoll.i`. Follow the specific instructions in the SWIG documentation to build your own binding.
Note: The current bindings do not return a result directly - You should read from the file that is generated.

### Shared Library
Many languages allow importing of code via shared object. You can find this .so file in the build folder after running `make all`
