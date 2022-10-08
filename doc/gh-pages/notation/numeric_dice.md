---
title: Numeric Dice
published: true
nav_order: 1
---

# Numeric Dice


{: .story }
>**GM** (Game Master): Okay, Welcome to the game. Let's get started. You've just received a contract to explore a nearby dungeon. Roll a d5 and it'll take that many days."
>
>**Grindon the Brave**: "d5"
>
>*GNOLL*: 3
>
>**GM**: Okay, you should have enough supplies for that trip. Saddle up and let's go!
>
>**Grindon the Brave**: Onward to adventure! I'll pick up a book in the store to read on the road!
>
>**GM** There's a few book shops around here, That'll be 2d4 gold pieces when you eventually find an interesting one
>
>*GNOLL*: 7
>
>**Grindon the Brave**: "Ugh. Expensive, but it is a signed copy at least!"
>
>**GM**: You catch the next wagon out of town and buildings start changing into fields of wheat and barley as it moves out. The journey is long and... "z4"
>
>*GNOLL*: 0
>
>**GM** Uneventful! You make it to the dungeon unabated. However, at the entrance stands.. d{2,4,5}
>
>*GNOLL*: 2
>
>**GM** Two goblins! Dressed up in rusted armour and bent weaponry, as if protecting the entrance.

What will happen next? [Continue to the next chapter!](Symbolic-Dice)


## Basic Numeric Dice

The basic form of a dice roll is *x***d***y* where *x*, *y* ∈ ℤ<sup>+</sup>.

In plain english, this means that *x* and *y* are positive whole numbers (e.g. 1, 7, 138).

The value *x* is the number of dice that you wish to roll. You can exclude this, and it'll be assumed you mean a single die.

The value *y* tells us how many sides the dice has. A regular six-sided die can be called a "d6". You can't exclude this value, because we won't be able to tell how many sides the dice has!

### Numeric Dice Examples

- `1` - A Constant Value. It will just return the value "1"
- `1d4` - A Single Die Roll with 4 Sides. It will return a value between 1 and 4.
- `d4` - This is the same as above, as **x** is assumed to be 1.
- `2d4` - Roll 2 Dice with 4 Sides. It will return a value between 2 and 8.
- `d` - This will return an error because there is no y term.

{: .explanation}
> The *x***d***y* notation is one aspect of dice notation that is common for almost every application, so we don't have to make any choices here!
>
> D without y (as seen in the last example) can default to a set number of sides if a game system only uses one type of dice. However, this default can change between games so as a generic notation we do not assume a value.

## Zero Bias Notation

It is assumed that the values on a dice start from 1. (e.g. a d6 dice would have values 1,2,3,4,5,6). Zero-Bias notation allows your dice to start from zero instead (e.g. z6 would have values 0,1,2,3,4,5).

Rolling behaviour is identical to using 'd' for symbolic dice.

{: .explanation}
> There is inconsistency in various dice notation on how to represent zero-bias notation.
>
> Alternative representations include using a minus sign <sup>[ref](http://hjemmesider.diku.dk/~torbenm/Troll/manual.pdf)</sup> (i.e. d-6) but we consider this non-obvious as it could easy mean values from -1 to -6.
>
> It also conflicts with systems that have only one die and abbreviate from e.g. 2d6 to just "2d"

## Customizable Numeric Dice
In the case where you need non-standard die sides (that do not start from 0/1, or do not regularly increment by 1), a custom dice can be made specifying the allowed values in braces.

A simple prime number dice might look like d{2,3,5,7,11,13}.

Where numbers are all consecutive, one can use a hyphen to indicate a range e.g. a die with sides 10,11,12,13,14,15 could be written as d{10..15}. This notation includes both the given start and end values in the pool of rollable values.

### Customized Dice Examples
- d{} - produces an error for a die with no sides is not a die at all
- d{1,3..6} - produces a value between 1 and 6, but excluding 2

{: .explanation}
>
> With more complicated dice, brings more complicated syntax. However, we want to keep the syntax as straightforward as possible.
>
> We note however that there are sometimes easier ways to do these dice if you think about them. e.g. the latter dice could be represented as d6+9
>
> We choose .. instead of - to avoid confusion with minus math
