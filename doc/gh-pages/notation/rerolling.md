---
title: Rerolling
published: true
nav_order: 7
---

# Rerolling

```
   ⚔️ Grindon's Tale
   
   GM: Well, you took a load of damage, but you did level up.
   Grindon: Nice, I get my class feature - I can reroll 1s!
   GM: Do you remember how to do that?
   Grindon: Yep, I just do a "1d20r#1"
   GNOLL: [9]
   GM: Great. Remember, you could still get a 1 on your second roll.
   Grindon: Yeah, but then I deserved it.
```

Rerolling is often based on conditions (e.g. reroll if result is a 1). There are two options when using these conditions
 - Reroll once 
 - Reroll until the condition is no longer true.

We represent these as "r" and "R" respectively.


## Repeat Dice Rolls
If you wish to run the same thing several times, you can use "xN" to re-do an operation. Note that this will produce N results, not 1.


## Conditional Rolling

*Under Construction*

<!--
```
   GM: There's a set of 4 levers on the wall, they seem to control the gate blocking you from the next room
   Grindon The Brave: I randomly pull them up and down
   GM: Uh.. Okay - Roll some fate die and if you get a "+" it's in the right position
   Grindon The Brave: Cool - "4dFc"
   GNOLL: [2]
   GM: The gate shudders, but remains still
   Grindon The Brave: Ugh, I hate puzzles. I'll just hit it with my axe..
   GM: *Sigh*...
```

Some systems may get you to roll subsequent rolls on certain conditions. For example, if you roll a 1 on a d20, maybe your magic spell explodes, causing 1d6 damage to everyone around them. To express this we use conditions.

These follow a *ternary* syntax, which is to say:
> initial_roll_and_condition[do_if_condition_met|otherwise_do_this]
> d20#1[d6|p]

There are some key-letters which may be used:
 - **P** - Persist. Use the initial Roll again
 - **S** - Scrap. Remove the initial roll (if there is no other value mentioned, 0 will be the result value) 
-->
