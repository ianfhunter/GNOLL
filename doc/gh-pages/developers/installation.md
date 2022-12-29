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

## Commandline Installation 

GNOLL can be installed into your user path for convenience. 
This will allow parsing of dice notation from the command line.

```bash
make install
dice "1d20"
```

**Note:** Some command line syntax may conflict with tokens used in Dice Notation (e.g. >). Please escape or quote your notation to avoid this issue.

There is at present no capacity for enabling or disabling optional features via the command line app. See Issue [#431](https://github.com/ianfhunter/GNOLL/issues/431)

## Language Bindings 

We have tested binding GNOLL for use in several programming languages.

The following documentation intention is not to be exhaustively compatible with every revision of a programming language (as that is a large overhead to maintain), but to be used as a helpful reference for setting up GNOLL for your own software.

### C
C is the default build target and what GNOLL is written in.

Tested with GCC and Clang Compilers and C99 compliant.

- Your application's build scripts should be modified to link against the shared object created with `make all` and to include the path to the folder containing `shared_header.h`
- In your C code, include the "shared_header.h" file and the `roll_full_options` function will be available to use as described above.

To make the example C application:
```bash
make all
./build/dice "1d20"
> Result: 14;
```

The sourcecode for the C application is in the [grammar folder under src](https://github.com/ianfhunter/GNOLL/tree/main/src/grammar). It contains the core GNOLL logic as well as the application logic.

### C++
Tested with Clang Compiler, Ubuntu 22.04.

- Your application's build scripts should be modified to link against the shared object created with `make all` and to include the path to the folder containing `shared_header.h`
- In your C++ code, include the "shared_header.h" file and the `roll_full_options` function will be available to use as described above.

[An example application](https://github.com/ianfhunter/GNOLL/tree/main/src/C%2B%2B) is available (hardcoded to roll a d20):
```bash
make cpp
...
> 19 
```

### CSharp
Tested with Mono Compiler, Ubuntu 22.04

The [C# example](https://github.com/ianfhunter/GNOLL/tree/main/src/CSharp) expects that the shared object libdice.so is generated under `build/`.
The `build/` directory may need to be added to the environment variable `LD_LIBRARY_PATH`.

The library is imported and the `char *`s of the C function are managed to consume C# Strings ([via marshalling Unmanaged LPStrs](https://github.com/ianfhunter/GNOLL/blob/22b2f9248417cb756818cb5850dc20c4f77fde0e/src/CSharp/main.cs#L7))

The example application creates a RollWithGNOLL function which handles all the file parsing. The application calls this function with a hardcoded '1d20'.

```bash
make cs
...
> 4
```

Function example:
```cs
RollWithGNOLL("1d20")
...
5
```

### Go
Tested with Golang 1.18, Ubuntu 22.04

The Go setup is very similar to the C# example, in that we must ensure the build directory has the libdice.so file and that the build directory is in `LD_LIBRARY_PATH`.
Apart from this, the steps to execute your go application (e.g. `go build` and `go run`) should remain unchanged.
The application is hardcoded to parse a d20 roll.
```bash
make go
...
> 17
```

The code itself creates "CStrings" which the developer must be careful to free after use. 

### Haskell
Tested with ghc 9.4.3, cabal 3.0.0.0-3build1.1, Ubuntu 22.04

In [this example](https://github.com/ianfhunter/GNOLL/tree/main/src/haskell), libdice.so is installed to /usr/lib/ and the cabal build configuration points to it's location via the 'extra-libraries' field.
In the main application, GNOLL is imported via the Foreign Function Interface (`foreign import`). You must use the CStrings structures rather than native haskell strings.

```
make haskell
cabal run src [dice roll e.g. d20]
```

### Python
Available from [PyPi](https://pypi.org/project/gnoll/)
Tested with Python3.10, Ubuntu 22.04

Install via Pip:
```bash
pip install gnoll
```
Then you can import the `roll` function and the custom Exceptions `GNOLLExceptions` which the function can raise.
```python
from gnoll import roll
roll("2d100")
> (0, [[108]] ,None)
```
The roll function takes the form:
```python
def roll(s,
         verbose=False,
         mock=None,
         mock_const=3,
         breakdown=False,
         builtins=False):
```
Where `s` is the string containing the dice notation and the other optional fields correspond with the optional features as mentioned above.
File management is handled internally and is hidden from the caller.

Exceptions are all of the Exception type `GNOLLException` and follow the [list of errors](developers/errors.html)

If you are running from sourcecode:
```bash
make python
```
will build the application to expose the same interface.

### Perl
Tested on Perl 5.30, Ubuntu 20.04

The [Perl example](https://github.com/ianfhunter/GNOLL/tree/main/src/perl) uses the SWIG framework to create its bindings.
The Perl libraries must be linked at build time ($PERL_VERSION can be set to configure this (default: 5.30)).
GNOLL's notation parsing is then exposed via a `gnoll::roll_and_write` function (a wrapper around roll_full_options which has all options set to False).

```bash
make perl
...
> 20
```


### Java
Tested with openjdk-8, Ubuntu 22.04

Java, like Perl, must have GNOLL compiled with its language headers.

This can be done with the make command:
```bash
make java
```

Afterwards, GNOLL'S functionality is available via a `DiceNotationParser.roll` function which takes a dice notation string and a filename and performs as usual.

### Julia
Tested on Ubuntu 20.04, Julia 1.4.1

Whether installing from [JuliaHub](https://juliahub.com/ui/Packages/GnollDiceNotation/WetJc/) or from source with 
```
make julia
```
The function `GnollDiceNotation.roll` is available to use, which simply takes in a dice notation string.

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

As the c code is being compiled to JavaScript, it operates in the same way

### PHP
Tested on PHP 8.1.13, Ubuntu 22.04

As long as the shared object is in LD_LIBRARY_PATH, you can use the functions from c with PHP's cdef
```
FFI::cdef(
    "int roll_and_write(char * roll, char *fn );",
    "libdice.so"
);
```

The [PHP Example] (https://github.com/ianfhunter/GNOLL/blob/main/src/PHP/index.php) parses a hardcoded 3d6 roll.
```bash
make php
```

### R
Tested on R 4.2.2, Ubuntu 22.04


#### Setup 
Generate the shared object file that R can consume.
```bash
make r
```

Inside `main.r` we show an example of GNOLL usage.

- Load in the shared object
- Delete the temporary file that contains GNOLL output
- Call GNOLL
- Parse result

#### Notes
This example uses the .C function which is usually not recommended. The recommended way to call C code in R is through the .Call() function. See [#368](https://github.com/ianfhunter/GNOLL/issues/368)


### Ruby
Tested on Ruby 3.0, Ubuntu 22.04

Using Ruby's native FFI code, the [demo application](https://github.com/ianfhunter/GNOLL/blob/main/src/ruby/main.rb) creates a namespaces function for usage. `DiceNotation.roll([dice notation string])`

```bash
make ruby
```

## Something Else?
### SWIG
The swig bindings are already generated for you in `src/swig/gnoll.i`. Follow the specific instructions in the SWIG documentation to build your own binding.
Note: The current bindings do not return a result directly - You should read from the file that is generated.

### Shared Library
Many languages allow importing of code via shared object. You can find this .so file in the build folder after running `make all`
