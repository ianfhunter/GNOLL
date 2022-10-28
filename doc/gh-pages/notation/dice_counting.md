---
title: Dice Counting
published: true
nav_order: 8
parent: Dice Notation
---

# Dice Counting

{: .story}
>**GM**: The room ahead of you is clear now
>
>**Grindon**: Great, I continue deeper into the dungeon. I'll run and get there faster
>
>**GM**: Don't forget to check those corridors! The ground slips from under you and spikes appear below!
>
>**Grindon**: Oh no! Can I run along the wall?
>
>**GM**: Sure. You'll need to get your feet on 2 secure parts of the wall to make it. Let's say you have 3 seconds (3 dice) and you need to get at least a 5 on each dice
>
>**Grindon**: at least a 5?! Aw man, I'm ruined!  3d6f>5c
>
>*GNOLL*: [2]
>
>**GM**: Great. Remember, you could still get a 1 on your second roll.
>
>**Grindon**: Yeah, but then I deserved it.

## Counting Dice

In several games, the rolls may not be a matter of *if* your total of rolls is good, but *how many* good rolls you have.
For this, we count the number of successes, according to a criteria. By default a max-face value is assumed to be a success, but you can change this, much like other condition changes.

Count how many D10s are larger than 7:
>10d10f>7c

Count how many Fate dice are '+':
>100dFc

{: .explanation }
> Counting dice is a rarer feature of dice rollers and there is at least one instance of using the '#' symbol to denote this operation [[1]](https://www.sophiehoulden.com/dice/documentation/notation.html#count)
> Other dice rollers merge the functionality with filtering[[2]](https://www.critdice.com/blog/2016/10/30/critdice-version-20-released). However, this limits the utility of the filtering operation.
>
> As we already use # for Macro Setting, we chose to use 'c' standing for 'count' which we believe is more straightforward anyhow.

## Counting Successes / Failures

GNOLL does not support the higher level understanding of the result of dice rolls.

{: .explanation }
> Some level of this behaviour can be determined using filters and counts (e.g. count all rolls above 10). However, eeabling this sort of checking within GNOLL would also mean we would have to consider 'degrees of success' and other higher level interpretation of dice rolls, rather than just the rolled result. This would require a large extension of GNOLL's scope.
>
> See also the [issue discussion for Degrees of Success](https://github.com/ianfhunter/GNOLL/issues/48)
