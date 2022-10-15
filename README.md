# GNOLL
[![Build + Test](https://github.com/ianfhunter/GNOLL/actions/workflows/c-cpp.yml/badge.svg)](https://github.com/ianfhunter/GNOLL/actions/workflows/c-cpp.yml)
[![Test: Perl](https://github.com/ianfhunter/GNOLL/actions/workflows/perl-test.yml/badge.svg)](https://github.com/ianfhunter/GNOLL/actions/workflows/perl-test.yml)
[![Test: JavaScript](https://github.com/ianfhunter/GNOLL/actions/workflows/js-test.yml/badge.svg)](https://github.com/ianfhunter/GNOLL/actions/workflows/js-test.yml)
[![Test: Go](https://github.com/ianfhunter/GNOLL/actions/workflows/go-test.yml/badge.svg)](https://github.com/ianfhunter/GNOLL/actions/workflows/go-test.yml)

[![CodeFactor](https://www.codefactor.io/repository/github/ianfhunter/gnoll/badge)](https://www.codefactor.io/repository/github/ianfhunter/gnoll)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/90add1388135474a928b715ddbb071b4)](https://www.codacy.com/gh/ianfhunter/GNOLL/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ianfhunter/GNOLL&amp;utm_campaign=Badge_Grade)

[![status](https://joss.theoj.org/papers/c704c5148e622d32403948320c5e96a1/status.svg)](https://joss.theoj.org/papers/c704c5148e622d32403948320c5e96a1)
[![TTRPG compatibility rate](https://img.shields.io/badge/Popular%20TTRPG%20compatibility-96.875%25-green)](https://img.shields.io/badge/Popular%20TTRPG%20compatibility-96.875%25-green)
[![GitHub license](https://img.shields.io/github/license/ianfhunter/GNOLL.svg)](https://github.com/ianfhunter/GNOLL/blob/master/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/ianfhunter/GNOLL.svg)  [![Donate](https://img.shields.io/badge/Donate-Paypal-yellow.svg)](https://paypal.me/ianfhunter)

<p align="center">
 <img src="https://raw.githubusercontent.com/ianfhunter/GNOLL/main/media/gnoll_halloween.png" height="200">
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

We wrote GNOLL to be the definitive solution to dice notation. We've written all the code in C, but fear not! You can use GNOLL in the following languages too:

- C / C++
- Python
- Perl
- Go
- JavaScript (Node.js)

 We have plans to add more example integrations of GNOLL's through different languages in the near future. Let us know if you have any particular wants!

Tested on Linux (Ubuntu) and Windows (10, WSL).

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

There's so many different things, we'd bore you to list them all here. For the specific details of supported notation, [check out our documentation](https://www.ianhunter.ie/GNOLL).

## Getting Started
### Usage from a package manager
#### Python
```bash
pip3 install GNOLL
```

Then, in your code:
```python
from gnoll.parser import roll
roll("1d20")
>> 7
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
$ ./dice 1d20
20
```
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

## 🏗️ Built With

  - [Lex & Yacc](http://dinosaur.compilertools.net/) - Grammar Lexing & Parsing
  - [uthash](https://troydhanson.github.io/uthash/userguide.html) - C hashtable lib
  - Love! 💖

## 💰 Donate

[Keep this project alive](https://ko-fi.com/ianfhunter)
