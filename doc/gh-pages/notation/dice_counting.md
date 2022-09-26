---
title: Dice Counting
published: true
nav_order: 8
---

# Dice Counting

{: .story}
>   GM: The room ahead of you is clear now
>
>   Grindon: Great, I continue deeper into the dungeon. I'll run and get there faster
>
>   GM: Don't forget to check those corridors! The ground slips from under you and spikes appear below!
>
>   Grindon: Oh no! Can I run along the wall?
>
>   GM: Sure. You'll need to get your feet on 2 secure parts of the wall to make it. Let's say you have 3 seconds (3 dice) and you need to get at least a 5 on each dice
>
>   Grindon: at least a 5?! Aw man, I'm ruined!  3d6f>5c
>
>   GNOLL: [2]
>
>   GM: Great. Remember, you could still get a 1 on your second roll.
>
>   Grindon: Yeah, but then I deserved it.

## Counting Successes

In several games, the rolls may not be a matter of *if* your total of rolls is good, but *how many* good rolls you have.
For this, we count the number of successes, according to a criteria. By default a max-face value is assumed to be a success, but you can change this, much like other condition changes.

> 10d10f>7 - Count how many D10s are larger than 7

> 100dFc - Count how many Fate dice are +

{: .explanation }   
> Some games have a specific concept of success counting
>
> However, enabling this sort of checking within GNOLL would also mean we would have to solve 'degrees of success' and other higher level interpretation of dice rolls, rather than just the rolled result.
>
> Therefore, GNOLL just counts dice and the use of [filters](https://www.ianhunter.ie/GNOLL/notation/filters.html) can emulate this behaviour.
>
> See also the [issue discussion for Degrees of Success](https://github.com/ianfhunter/GNOLL/issues/48)