---
title: Dice Shorthand
published: true
nav_order: 3
---

# Dice Shorthand


{: .story }   
> Grindon: Alright, before I crawl through the chimney, I'm going to look down it to check it's safe
>
> GM: There are the remains of a fire, but it looks safe to descend
>
> Grindon: Great! Onwards!
>
> GM: You crawl down the sooty chimney, getting well and truly covered in black dust. Stepping into the fireplace below, you find... d%
>
> GNOLL: [74]
>
> GM: *Consults Table* "A half-burnt wooden doll that looks eerily familiar. It looks like... you!"
>
> Grindon: That's.. unsettling... I thought my ears were burning earlier.. 

## Numeric Dice
d% is often be used in place of a d100

## Fate Dice

Instead of a normal N-sided dice, your game may use 'Fate'-style dice. These dice are generally 6 sided with the values ('-', '-', ' ', ' ', '+', '+'. (Equivalent to a three sided dice).
Internally these values are treated as -1, 0 and +1.

To use Fate dice, the syntax supports the following:
 - **dF** - a single Fate die
 - **1dF** - a single Fate die
 - **2dF** - multiple Fate die

## Alternative Fate Dice

Some systems represent Fate dice as U instead of dF. dF is the most popular choice so we have chosen to stick with it.
Additionally you might find "dF.1", "dF.2" and "dF.3" elsewhere. These expand to:

- dF.3 - [+,+,+,-,-,-] 
- dF.2 - [+,+,-,-,0,0] (This is the same as the usual 'dF')
- dF.1 - [+,0,-,0,0,0]

As the number indicates how many plus and minus symbols to have on the dice, any number larger than 3 is treated as dF.3

## Others

Occasionally just 'c' is used for a HEADS, TAILS flip of a dice. GNOLL also supports this syntax.

If there is a common shorthand you are aware of that is not implemented you can file an issue or you can define custom dice by [Creating Custom Macros](./custom_macros.html). Less common ones may be accepted as [Built-In Macros](./builtin_macros.html).
