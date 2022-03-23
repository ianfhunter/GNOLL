<p align="center">
<img src="media/logo.png" height="200">
</p>

<!--
<p align="center">
   <a href="site/demo.html">Try out our demo (Warning: Non-Functional)</a>

   <a href="https://discord.gg/NkDwYbU">Join our Discord</a>
</p>
--->

A comprehensive grammar and libraries for Dice-based RPG systems

In other terms, A language for parsing [Dice Notation](https://en.wikipedia.org/wiki/Dice_notation), that you can plug into your own dice-based projects

```
   Gridon The Brave: I want to steal from the goblin sitting at the counter
   GM: Okay, give me a stealth check!
   Gridon The Brave: Okay, that's a "1d20+5"
   [Dice]: 25
   GM: You successfully pickpocket the goblin - but all he had were some crummy dice...
```

[Follow Grindon's adventure through the dice syntax in our Wiki](https://github.com/ianfhunter/dice-tower/wiki/Dice-Roll-Syntaxes)

## Current Status

### Build & Test

[![Build status](https://ci.appveyor.com/api/projects/status/jyx709w6f69dvy8s?svg=true)](https://ci.appveyor.com/project/ianfhunter/dice)

### Quality
<!-- [![Coverage Status](https://coveralls.io/repos/github/ianfhunter/dice-tower/badge.svg?branch=master)](https://coveralls.io/github/ianfhunter/dice-tower?branch=master) -->
<!-- [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2797/badge)](https://bestpractices.coreinfrastructure.org/projects/2797)
![CII Best Practices Tiered Percentage](https://img.shields.io/cii/percentage/2797.svg?label=CII%20Best%20Practises)
[![Security Scanner](https://img.shields.io/badge/Security%20Scanner-DeepCodeAI-ff69b4.svg)](https://www.deepcode.ai)
![Maintainability](https://img.shields.io/codeclimate/maintainability-percentage/ianfhunter/dice-tower.svg)
![Complexity Issues](https://img.shields.io/codeclimate/issues/ianfhunter/dice-tower.svg)
![Technical Debt](https://img.shields.io/codeclimate/tech-debt/ianfhunter/dice-tower.svg) -->


### Meta
[![GitHub license](https://img.shields.io/github/license/ianfhunter/dice-tower.svg)](https://github.com/ianfhunter/dice-tower/blob/master/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/ianfhunter/dice-tower.svg)
![GitHub Community Standards](https://img.shields.io/badge/Github%20Community%20Standards-100%25-green.svg)

[![Donate](https://img.shields.io/badge/Donate-Paypal-yellow.svg)](https://paypal.me/ianfhunter)

### Language Support

Several languages will be targetted as the project develops. Interested in something in particular? [Vote on FeatHub](https://feathub.com/ianfhunter/dice).

Primary Support:
 - Commandline
Secondary Support:
 - Python
 - C
Tertiary Support:
 - Javascript
 - PHP
 - Ruby

The rationale for this is to enable general development, but also promote the usage for webapps.
 
## Getting Started

Get up and started with the project locally for integration into your own project, or just to mess around with it.
More comprehensive setup guide available on [the Wiki](https://github.com/ianfhunter/dice-tower/wiki)

### Prerequisites

The following details are for Ubuntu 18.04 or higher. Visit the wiki for other platforms (note: nothing there yet)
```
sudo apt-get install bison flex
```

### Building

Compile the binary executable

```
make all
```

Add to path so you can refer to it easily. 

```
export PATH=$PATH:/path/to/dir/
```

You should be able to try out rolling some dice now!
(Note: currently you need to pipe a file into the program)
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

### Meta Tests (not currently working)

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

* [Lex & Yacc](http://dinosaur.compilertools.net/) - Grammar Lexing & Parsing
* [Hatchful](https://hatchful.shopify.com/onboarding/select-logo) - Logo Creation Tool
* Love 💖

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ianfhunter/dice-tower/tags). 

## Authors / Contributers / Attributions

* **Ian Hunter** - *Main Developer* - [Ianfhunter](https://github.com/ianfhunter/)

See also the list of [contributors](https://github.com/ianfhunter/dice-tower/contributors) who participated in this project.


## Issues / Bugs / FAQs / Feature Requests

We are currently building a Wiki to help you in building on top of Dice. 
In the meantime, if you encounter any issues, please file them in our [Issue Tracker](https://github.com/ianfhunter/dice-tower/issues).
You can vote on prospective new features on [FeatHub](https://feathub.com/ianfhunter/dice)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

Individiual arrangements can be made if this is an issue for your project - Contact Me at [LinkedIn](https://www.linkedin.com/in/ianfhunter) to discuss.

## Acknowledgments

* **Billie Thompson** - *README & Contribution Templates* - [PurpleBooth](https://github.com/PurpleBooth)

## Donate

[Keep this project alive](https://paypal.me/ianfhunter)
