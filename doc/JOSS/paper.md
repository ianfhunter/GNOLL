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

Dice Notation is a system for describing how to roll collections of dice. It is often used to assist understanding of rules of games - particularly tabletop roleplaying games. Existing research software in this space has been primarily designed for other researchers and statisticians despite the fact that a large population of those actually playing these games are young [@DNDDemographics2019] or not involved in statistical research.

GNOLL is a software library for dice notation — A method of describing how to roll collections of dice. GNOLL’s dice notation syntax is focused on parsing a language that tabletop role-players and board gamers already use for specifying dice rolls in many popular software applications. Existing implementations of such a syntax are either incomplete, fragile, or proprietary, meaning that anyone hoping to use such syntax in their application likely needs to write their own solution. GNOLL offers researchers and engineers a multi-lingual implementation that can serve as a reference for this style of notation, 

GNOLL is an open-source project using the compilation tool ‘YACC’ and lexical tool ‘LEX’ which can be integrated into many applications with relative ease. This paper explores GNOLL’s extended dice notation syntax and its competitive performance

# Statement of Need
Whilst there are several dice rolling utilities on the market for research/commercial use there is no current solution which is:
- Open source 
- Using a low level language like C for maximal integration
- Multiple language bindings
- supporting multiple notation standards
- supporting non-simplex combinations of notation. 

While some solutions may offer one or two of these, GNOLL addresses all of these points.

# Mathematics
GNOLL builds upon actual use-cases of how dice are specified in software, rather than theoretical mathematical notations.
The simplest of these representations is {x}d{y} where x and y are integers. This asks that we roll X number of Y-sided dice. e.g. 3d6 would be requesting 3 6-sided dice.



# Citations

# Figures

# Acknowledgments
Thank you to the TTRPG community for creating all of your adventures, art and silly accents.
I would like to acknowledge my dog for sitting on my lap throughout.

# References
