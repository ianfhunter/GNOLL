# GNOLL

[![Test: Functionality](https://github.com/ianfhunter/GNOLL/actions/workflows/test_core.yml/badge.svg)](https://github.com/ianfhunter/GNOLL/actions/workflows/test_core.yml)
[![Test: Language Bindings](https://github.com/ianfhunter/GNOLL/actions/workflows/test_language_bindings.yml/badge.svg)](https://github.com/ianfhunter/GNOLL/actions/workflows/test_language_bindings.yml)
[![Test: OS Support](https://github.com/ianfhunter/GNOLL/actions/workflows/test_OS.yml/badge.svg)](https://github.com/ianfhunter/GNOLL/actions/workflows/test_OS.yml)

[![CodeFactor](https://www.codefactor.io/repository/github/ianfhunter/gnoll/badge)](https://www.codefactor.io/repository/github/ianfhunter/gnoll)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/90add1388135474a928b715ddbb071b4)](https://www.codacy.com/gh/ianfhunter/GNOLL/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ianfhunter/GNOLL&amp;utm_campaign=Badge_Grade)

[![status](https://joss.theoj.org/papers/c704c5148e622d32403948320c5e96a1/status.svg)](https://joss.theoj.org/papers/c704c5148e622d32403948320c5e96a1)
[![TTRPG compatibility rate](https://img.shields.io/badge/Popular%20TTRPG%20compatibility-98.66%25-green)](https://img.shields.io/badge/Popular%20TTRPG%20compatibility-96.875%25-green)
[![GitHub license](https://img.shields.io/github/license/ianfhunter/GNOLL.svg)](https://github.com/ianfhunter/GNOLL/blob/master/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/ianfhunter/GNOLL.svg)  [![Donate](https://img.shields.io/badge/Donate-Paypal-yellow.svg)](https://paypal.me/ianfhunter)

<p align="center">
 <img src="https://raw.githubusercontent.com/ianfhunter/GNOLL/main/media/gnoll.png" height="200">
</p>

An easy to integrate [dice notation](https://en.wikipedia.org/wiki/Dice_notation) library for multiple programming languages.
Use for instant support of common syntax and a library that can scale with your demands, rather than a sticky taped monstrousity of regular expressions and tears.

Here's an example of how you might use GNOLL:
```markdown
**Grindon The Brave**: I want to steal from the goblin sitting at the bar.
**Dungeon Master**: Okay, give me a stealth check!
**Grindon The Brave**: Okay, that's a <1d20+5>
[GNOLL]: 21
**Dungeon Master**: Hurrah! You successfully pickpocket the goblin! However, all he had in there were some crummy dice...
```

[You can follow Grindon's full adventure through the world of dice notation in our Documentation](https://www.ianhunter.ie/GNOLL).

Many of our notation design decisions are explained in the documentation and compared to other dice notation parsers.

## Current Status
### 🧑‍💻 Language Support

GNOLL was written to be the definitive solution to dice notation. The core has been written in C, but fear not! You can use GNOLL in many other programming languages too.

![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=c-sharp&logoColor=white)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Haskell](https://img.shields.io/badge/Haskell-5e5086?style=for-the-badge&logo=haskell&logoColor=white)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Julia](https://img.shields.io/badge/-Julia-9558B2?style=for-the-badge&logo=julia&logoColor=white)
![Lua](https://img.shields.io/badge/lua-%232C2D72.svg?style=for-the-badge&logo=lua&logoColor=white)
![Perl](https://img.shields.io/badge/perl-%2339457E.svg?style=for-the-badge&logo=perl&logoColor=white)
![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white)
![Ruby](https://img.shields.io/badge/ruby-%23CC342D.svg?style=for-the-badge&logo=ruby&logoColor=white)
![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)

Primarily tested on Linux (Ubuntu), but functional in various forms on Windows (10, WSL) and Mac.

### 🎲 Dice Notation
- XdY notation
- Arithmetic
- Fate Dice
- Miscellaneous Symbolic Dice
- Shorthands & Macros
- Alternate Syntax
- Explosions
- Drop/Keep
- Rerolling
- Filtering
- Functions

There's so many different things, we'd bore you to list them all here. For the specific details of supported notation, [check out our documentation](https://www.ianhunter.ie/GNOLL).

## Getting Started
### Usage from a package manager
#### Python
```bash
pip3 install GNOLL
```

Then, in your code:
```python
from gnoll import roll
roll("1d20")
>> (0, [[12]], None)
# (return code, final result, dice breakdown (if enabled))
```

Or, use the command-line interface (see `--help`):
```sh
$ python3 -m gnoll 2d4
6
$ function gnoll() { python3 -m gnoll --breakdown "$@" ; }
$ gnoll 3d6 + 10
[5, 5, 4] --> 24
```

### 🛠️ Installing From Source
#### Basic Requirements
```bash
sudo apt-get install bison flex make python3-pip -y
pip install -r reqs/requirements.txt
make all
```

To verify your setup, try our tests:
```bash
make test
```
Or, just try some commands yourself!

```bash
$ ./build/dice 1d20
20
```
If you would like to run the 'dice' command from anywhere, use `make install` to add the executable to your path.

(Note that not all commands may not be able to be used this way as some symbols are reserved for use by different terminal interfaces (e.g. bash uses ! and #))

For languages other than Python/C/C++ call the corresponding make target after the commands above.

## 🐛 Issues / Bugs / FAQs / Feature Requests

If you encounter any issues or have any ideas, please file them in our [Issue Tracker](https://github.com/ianfhunter/GNOLL/issues).

## ✋ Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## 🔢 Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ianfhunter/gnoll/tags).

## 🤹 Authors / Contributers / Attributions

  - **Ian Hunter** - *Main Developer* - [Ianfhunter](https://github.com/ianfhunter/)

See also the list of [contributors](https://github.com/ianfhunter/gnoll/contributors) who participated in this project.

## 📃 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

Individual licensing arrangements can be made if this is an issue for your project - Contact Me at [LinkedIn](https://www.linkedin.com/in/ianfhunter) to discuss.

## 👏 Acknowledgments

  - **Billie Thompson** - *README & Contribution Templates* - [PurpleBooth](https://github.com/PurpleBooth)
  - [Markdown Badges](https://github.com/Ileriayo/markdown-badges)

## 🏗️ Built With

  - [Flex & Bison](https://aquamentus.com/flex_bison.html) - Grammar Lexing & Parsing
  - [uthash](https://troydhanson.github.io/uthash/userguide.html) - C hashtable lib
  - [PCG](https://www.pcg-random.org/) - Random Number Generation
  - [Arc4Random](https://www.freebsd.org/cgi/man.cgi?query=arc4random) - Random Number Generation (Cryptographically secure)
  - Love! 💖

## 💰 Donate

[Keep this project alive](https://ko-fi.com/ianfhunter)
