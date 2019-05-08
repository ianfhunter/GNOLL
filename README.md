# Dice 

<p align="center">
<img src="logo.png" width="200" height="200">
</p>

A comprehensive grammar and libraries for Dice-based RPG systems

In other terms, A language for parsing [Dice Notation](https://en.wikipedia.org/wiki/Dice_notation), that you can plug into your own dice-based projects

```
   Gridon The Brave: I want to steal from the goblin sitting at the counter
   GM: Okay, give me a stealth check!
   Gridon The Brave: Okay, that's a "1d20+5"
   [Dice]: 25
   GM: You successfully pickpocket the goblin - but all he had were some crummy dice...
```


## Current Status

[![Build status](https://ci.appveyor.com/api/projects/status/jyx709w6f69dvy8s?svg=true)](https://ci.appveyor.com/project/ianfhunter/dice)
[![Coverage Status](https://coveralls.io/repos/github/ianfhunter/dice/badge.svg?branch=master)](https://coveralls.io/github/ianfhunter/dice?branch=master)
[![Requirements Status](https://requires.io/github/ianfhunter/dice/requirements.svg?branch=master)](https://requires.io/github/ianfhunter/dice/requirements/?branch=master)
[![GitHub license](https://img.shields.io/github/license/ianfhunter/dice.svg)](https://github.com/ianfhunter/dice/blob/master/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/ianfhunter/dice.svg)

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2797/badge)](https://bestpractices.coreinfrastructure.org/projects/2797)
![CII Best Practices Tiered Percentage](https://img.shields.io/cii/percentage/2797.svg?label=CII%20Best%20Practises)
[![Security Scanner](https://img.shields.io/badge/Security%20Scanner-DeepCodeAI-ff69b4.svg)](https://www.deepcode.ai)

### Language Support

Currently available in python, though multi-language is desired

## Getting Started

Get up and started with the project locally for integration into your own project, or just to mess around with it.
More comprehensive setup guide available on [the Wiki](https://github.com/ianfhunter/dice/wiki)

### Prerequisites

The following details are for Ubuntu 18.04 or higher. Visit the wiki for other platforms (note: nothing there yet)
```
sudo apt-get install antlr4
pip3 install antlr4-runtime-something --user
```

### Installing

Getting Dice installed on your system (currently you can't do this)

Compile binary

```
make install
```

Add to path so you can refer to it easily. 

```
export PATH=$PATH:/path/to/dir/
```

You should be able to try out rolling some dice now!

```
$ dice 1d20
20
```

Critical Success!

## Running the tests

We aren't 100% complete just yet, You can run our test suite to see our current status

### Functionality Tests

```
$ make test
```

### Meta Tests

Code Coverage, Style Compliance, All those things that just make the world a little nicer.

```
$ make meta
```

## Deployment

Want to grab updates as they come in? Listen to our github releases for new content!
```
See https://gist.github.com/steinwaywhw/a4cd19cda655b8249d908261a62687f8
```



## Built With

* [ANTLR4](https://www.antlr.org/) - Grammar Parser
* ? - Logo Creator
* Love <3

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ianfhunter/dice/tags). 

## Authors / Contributers / Attributions

* **Ian Hunter** - *Main Developer* - [Ianfhunter](https://github.com/ianfhunter/)

See also the list of [contributors](https://github.com/ianfhunter/dice/contributors) who participated in this project.


## Issues / Bugs / FAQs / Feature Requests

We are currently building a Wiki to help you in building on top of Dice. 
In the meantime, if you encounter any issues, please file them in our [Issue Tracker](https://github.com/ianfhunter/dice/issues).
You can vote on prospective new features on [FeatHub](https://feathub.com/ianfhunter/dice)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

Individiual arrangements can be made if this is an issue for your project - Contact Me at [LinkedIn](https://www.linkedin.com/in/ianfhunter) to discuss.

## Acknowledgments


* **Billie Thompson** - *README & Contribution Templates* - [PurpleBooth](https://github.com/PurpleBooth)
