---
title: 'GNOLL: Efficient Multi-Lingual Software for Real-World Dice Notation and Extensions'
tags:
  - Python
  - Perl
  - C
  - C++
  - statistics
  - board games
  - ttrpgs
  - game design
authors:
  - name: Ian Frederick Vigogne Goodbody Hunter
    orcid: 0000-0003-3408-8138
    affiliation: 1
affiliations:
 - name: Independent Researcher
   index: 1
date: 26 August 2022
bibliography: paper.bib
---

# Summary

Dice Notation is a system for describing how to roll collections of dice. It is often used to assist understanding of rules of games - particularly tabletop roleplaying games (TTRPGs). Existing research software in this space has been primarily designed for other researchers and statisticians despite the fact that a large population of those actually playing these games are young [@DNDDemographics2019] or not involved in statistical research.

`GNOLL` is an open-source library for parsing commonly used dice notations - for use in gaming system research and/or software development. `GNOLL` is performant, supports most popular and obscure notations, has permissive licensing and is integratable into many other systems due to it being written in C.

# Statement of Need
Whilst there are several dice rolling utilities on the market for research/commercial use there is no current solution which:
- is open source / permissively licensed.
- can be easily integrated into other software despite language differences.
- provides reference for other implementations.
- supports such a diverse set of dice notation.

While some solutions may offer one or two of these points, GNOLL addresses all of them.

Without a larger project for reference/integration, many software developers have created their own dice notation parsers (for a simple subset is not too difficult to develop). These are usually sufficient for their immediate needs, but often create discrepencies in notation standards and do little to change this path for future developers.

# Related Reading

There are not many publications that specifically discuss dice notation. The most prominent papers are named `ROLL`[@ROLL] and `TROLL` [@TROLL]. To distinguish this research and still pay homage to the original work, GNOLL is a recursive acronym expanded from "GNOLL's Not *OLL". The reason for its distinction is that `GNOLL`'s notation is focused on real-world gaming usage of dice notation, whereas `ROLL` and `TROLL` are notations targetted at statistics research.

# Example Notation

There are many different operations and combinations of dice notation which cannot fit into the space constraints here, but are discussed in the project's [GitHub Wiki](https://github.com/ianfhunter/GNOLL/wiki/Dice-Roll-Syntaxes). A sample of the base dice notation has been described below.


The most basic dice roll in dice notation can be expressed as $$ x\textbf{d}y,\ where\ x,y\ \in{} \mathbb{Z}^{+}. $$ `x` dice are rolled with values from 1 to `y`. Where `x` is not specified, it is assumed that its value is 1. the exclusion of `y` produces an error (It is ambiguous to have a dice with no sides).

# Performance
`GNOLL` performs well against other dice rolling libraries available online both in terms of performance and functional coverage. In the Figures section below we show some simple benchmarking results against the `TROLL` system and a C++ parser and also test `GNOLL`'s Python interface against popular python packages and find that `GNOLL` is generally more performant. 

# Citations

# Figures
## Figure 1 - GNOLL Performance (C)

Comparison of `GNOLL`'s performance against other C/C++/SmallTalk dice notation parsers - [TROLL](http://hjemmesider.diku.dk/~torbenm/Troll/) and [E Bailey's 'Dice Parser'](https://github.com/EBailey67/DiceParser).

![A graph showing GNOLL's performance on different sizes of dice rolls. It is faster than TROLL and ROLL on each tick](C++.PNG)

## Figure 2 - GNOLL Performance (Python)

Comparison of `GNOLL`'s performance against other Python dice notation parsers. (Chosen from popular dice rollers on PyPi[@pypi] - ["Dice"](https://pypi.org/project/dice/), ["RPG Dice"](https://pypi.org/project/rpg-dice/), ["Python Dice"](https://pypi.org/project/python-dice/))

![A graph showing GNOLL's performance (via Python binding) on different sizes of dice rolls. It slightly underperforms for small sizes, but is faster than other python libraries for large sizes.](py.PNG)

# Acknowledgments
Thanks to my dog for the desk-side companionship and the demand for healthy stick-fetching breaks.
Thank you also to the various TTRPG publishers and online communities for enabling people all over the world to play make-believe together.

# References
