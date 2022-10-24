---
title: Drop/Keep Notation
published: true
nav_order: 5
parent: Dice Notation
---

# Drop/Keep Notation


{: .story }
>**GM**: Alright, you step over the goblin's corpse and go inside. There's another one there. He hasn't seen you yet.
>
>**Grindon The Brave**: I guess I should have talked to the other one, you were right. This one i will just stealth and put him to sleep.
>
>**GM**: It's pretty dark in here, so I'll give you advantage on a stealth roll
>
>**Grindon The Brave**: Nice, "2d20kh"
>
>*GNOLL*: [20]
>
>**GM**: You are the night itself. You take down the goblin before it can even react.


## Implementation Comparison

You might want to roll two dice and choose the higher or lower of the two in order to give you an *advantage* or *disadvantage*

There isn't a consistent way to express this and some of them can be ambigious.

| Platform   | Keep Highest/Drop Lowest | Keep Lowest/Drop Highest |
| ---------- | ------------------------ | ------------------------ |
| [Roll20](https://roll20.net/)     | 2d6kh                    | 2d6kl                    |
| [Rolz](https://rolz.org/)       | 2d6h                     | 2d6l                     |
| [OpenRoleplaying](http://openroleplaying.org/) | 2d6-L           | 2d6-H                    |
| [RoleGate](https://www.rolegate.com/)   | 2d6k                     | 2d6kl                    |
| [Dice.Run](https://dice.run/#/d/2d6d)   | 2d6k                     | 2d6d                     |
| [FoundryVTT](https://foundryvtt.com/) | 2d6max                   | 2d6min                   |
| [Avrae](https://avrae.io/)      | 2d6k1                    | 2d6p1                    |
| [DiceLogger](https://www.dicelogger.com/) | 2d6b1 | ? |

## GNOLL Syntax

GNOLL's Syntax is:

> [𝑘𝑑] [ℎ𝑙] 𝑧 𝑤ℎ𝑒𝑟𝑒 𝑧 ∈ Z<super>+</super>

e.g.
- 3d20kh2 - keep highest 2 rolls from 3 d20 rolls
- 3d20dl2 - drop lowest 2 rolls from 3 d20 rolls
- 3d20kl - keep lowest 1 (default if excluded) from 3 d20 rolls

{: .explanation }
> 'Keep' and 'Drop' are commonly used in feature documentation
>
> 'd' is sometimes avoided to avoid conflicting with the 'd' for defining a dice e.g. 'd6'
>
> GNOLL does not have this issue as a following term (l or h) are mandatory to avoid ambiguity.

## Other Types of Dropping

### Drop 'Middle'
GNOLL does not allow dropping a 'middle' dice as it will create unintuitive rules for handling odd/even dice like "upper-middle" or "lower-middle".
Instead, you can reproduce this by dropping both sides of a roll.

e.g. 3d20dl1dh1

### Drop Even/Odd
We suggest using [Filters](https://www.ianhunter.ie/GNOLL/notation/filters.html) for this type of logic and other types of conditional removal.
