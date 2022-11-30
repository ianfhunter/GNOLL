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
| Windows | WSL1 | Yes | No |
| MacOS | 12 | Yes | Error |

## Common Pre-requisites
```bash
sudo apt-get install bison flex make python3-pip -y
```

## Language Bindings 

### C
This is the default build target.
Tested with GCC and Clang Compilers.

```bash
make all
./a.out "1d20
```

### C++
Tested with Clang Compiler.

```bash
make cpp
```

### CSharp
Tested with Mono Compiler
```bash
make cs
```

### Go
```bash
make go
```

### Haskell
```
make haskell
```

### Python
Available from [PyPi](https://pypi.org/project/gnoll/)
```bash
pip install gnoll
```
If you are running from sourcecode:
```bash
make python
```

### Perl
```bash
make perl
```

### Julia
Available from [JuliaHub](https://juliahub.com/ui/Packages/GnollDiceNotation/WetJc/)
```
make julia
```

### JavaScript Setup

#### Pre-Requisites
```bash
sudo apt-get install emscripten nodejs
```

#### Build
```bash
make javascript
```

#### Run
```bash
node a.out.js
```

### R
```bash
make r
```

### Ruby
```bash
make ruby
```

## Something Else?
### SWIG
The swig bindings are already generated for you in `src/swig/gnoll.i`. Follow the specific instructions in the SWIG documentation to build your own binding.
Note: The current bindings do not return a result directly - You should read from the file that is generated.

### Shared Library
Many languages allow importing of code via shared object. You can find this .o file in the build folder after running `make all`
