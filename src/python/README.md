# GNOLL
[![Build + Test](https://github.com/ianfhunter/GNOLL/actions/workflows/c-cpp.yml/badge.svg)](https://github.com/ianfhunter/GNOLL/actions/workflows/c-cpp.yml) [![GitHub license](https://img.shields.io/github/license/ianfhunter/GNOLL.svg)](https://github.com/ianfhunter/GNOLL/blob/master/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/ianfhunter/GNOLL.svg)  [![Donate](https://img.shields.io/badge/Donate-Paypal-yellow.svg)](https://paypal.me/ianfhunter)

<!-- Dark and Light Mode switches -->
 <img src="https://raw.githubusercontent.com/ianfhunter/GNOLL/main/media/gnoll.png" height="200">


An easy to integrate [dice notation](https://en.wikipedia.org/wiki/Dice_notation) library for C, C++, Perl and Python.
Use for instant support of common syntax and a library that can scale with your demands, rather than a sticky taped monstrousity of regular expressions and tears.

Here's an example of how you might use GNOLL:
```markdown
   Grindon The Brave: I want to steal from the goblin sitting at the bar.
   Dungeon Master: Okay, give me a stealth check!
   Grindon The Brave: Okay, that's a <1d20+5>
   [GNOLL]: 21
   Dungeon Master: Hurrah! You successfully pickpocket the goblin! However, all he had in there were some crummy dice...
```

[You can follow Grindon's adventure through the world of dice notation in our Wiki](https://github.com/ianfhunter/GNOLL/wiki/Dice-Roll-Syntaxes)

## Current Status
### 🧑‍💻 Language Support

We wrote GNOLL to be the definitive solution to dice notation. We've written all the code in C, but fear not! We will be adding more wrappers for you to access GNOLL's functionality through different languages in the near future.

- C / C++
- Python
- Perl

Tested on Linux (Ubuntu) and Windows (10, WSL).

### 🎲 Dice Notation
- XdY notation
- Arithmetic
- Fate Dice
- Miscellaneous Symbolic Dice
- Macros 
- Explosions
- Drop/Keep

For the specific details of supported notation, [we've got a dedicated section in our wiki](https://github.com/ianfhunter/GNOLL/wiki/Dice-Roll-Syntaxes).
And feel free to ask for anything we're missing!

## Getting Started
### 🛠️ Prerequisites

- Linux 
- Windows (via WSL)

```bash
sudo apt-get install bison flex make python3-pip -y
make all
```

To verify your setup, try our tests:
```bash
   make test
```
Or, just try some commands yourself!

```bash
$ ./dice 1d20
20
```
(Note that not all commands may not be able to be used this way as some symbols are reserved for use by different terminal interfaces (e.g. bash uses ! and #))

```python
from gnoll.parser import roll
roll("1d20")
>> 7
```

## 🐛 Issues / Bugs / FAQs / Feature Requests

If you encounter any issues or have any ideas, please file them in our [Issue Tracker](https://github.com/ianfhunter/GNOLL/issues).

## ✋ Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## 🔢 Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ianfhunter/dice-tower/tags).

## 🤹 Authors / Contributers / Attributions

* **Ian Hunter** - *Main Developer* - [Ianfhunter](https://github.com/ianfhunter/)

See also the list of [contributors](https://github.com/ianfhunter/dice-tower/contributors) who participated in this project.

## 📃 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

Individiual licensing arrangements can be made if this is an issue for your project - Contact Me at [LinkedIn](https://www.linkedin.com/in/ianfhunter) to discuss.

## 👏 Acknowledgments

* **Billie Thompson** - *README & Contribution Templates* - [PurpleBooth](https://github.com/PurpleBooth)

## 🏗️ Built With

* [Lex & Yacc](http://dinosaur.compilertools.net/) - Grammar Lexing & Parsing
* [uthash](https://troydhanson.github.io/uthash/userguide.html) - C hashtable lib
* Love! 💖

## 💰 Donate

[Keep this project alive](https://ko-fi.com/ianfhunter)
