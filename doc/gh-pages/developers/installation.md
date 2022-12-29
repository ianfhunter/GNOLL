---
title: Setup
parent: Technical Information
published: true
nav_order: 0
---

# Setup

## Rolling with GNOLL 
### The core function

Each language binding example below will call the `roll_full_options` function, though some older examples may call deprecated functions which call that function internally.
If you are creating your own binding to GNOLL, use this function 

```c
int roll_full_options(
    char* roll_request, 
    char* log_file, 
    int enable_verbosity, 
    int enable_introspection,
    int enable_mocking,
    int enable_builtins,
    int mocking_type,
    int mocking_seed
);
```
The first parameter is the dice notation to be understood and computed. The result of which will be written into a file in the location `log_file`.
Then follows various optional values, which you should set to False (0) unless you wish to take advantage of the feature.

- `verbosity` is mostly useful for debugging a dice notation statement or for information during development. It will cause the execution to be slightly slower and is not recommended for release environments.
- `introspection` provides a per-dice breakdown of values rolled during the dice notation parsing. This is useful if you wish to display individual dice results and not just the final total. These values (if enabled) are added to the output file before the total.
- `mocking` is a feature allowing developers to generate predictable dice rolls for reproducible tests. This should only ever be used in a testing scenario.
- `builtins` are a collection of predefined [Macros](bad link) provided by GNOLL for ease of use. This comes with a performance trade-off of loading these macros prior to the given dice notation.

`mocking_type` is [an enum defining the behaviour of the Mocking logic](https://github.com/ianfhunter/GNOLL/blob/22b2f9248417cb756818cb5850dc20c4f77fde0e/src/grammar/util/mocking.h#L6). The `mocking_seed` provides the initial value to this logic, whether it be a random seed or an initialization of a predictably modified variable.

The return value of this function is one of the defined GNOLL [error codes](developers/errors.html).

### The output file

The output of GNOLL is a file which can be injected by a subsequent program, wether that be within the language binding itself to bind to more suitable structures or direct usage in downstream applications.
It is recommended that developers using GNOLL delete output files after they no longer need them 

The file consists of two parts:

- Dice introspection results (if enabled). The value for different dice are separated by commas and grouped by newlines (e.g. 3d6+2d6 would have 3 comma-seperated value on the first line, 2 comma-seperated value on the second line, followed by the final result)
- The final result of the dice notation, where discrete results are separated by a semicolon (e.g. 5d6;d6)

## OS Support 

| OS | Version | Tested (From Source) | Tested (PyPi) |
| -- | ------- | -------------------- | ------------- |
| Linux | Ubuntu 18.04 | Yes | Yes |
| Windows | WSL1 | Yes | Yes |
| Windows | Win11 | No | No |
| MacOS | 12 | Yes | Yes |

## Common System Pre-requisites
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
./build/dice "1d20"
> Result: 14;
```

Or, more conveniently;

```bash
make install
dice "1d20"
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
