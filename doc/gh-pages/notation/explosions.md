---
title: Explosions & Implosions
published: true
nav_order: 6
---

# Explosions & Implosions

{: .story }
>**Grindon**: Oh gosh, uh. What's in the room?! How close is the gnoll?
>
>**GM**: He's just coming through the door. There's a small table, a chest and some barrels of oil.
>
>**Grindon**: Oil! I light a torch and throw a match, diving back into the fireplace.
>
>**GM**: This is gonna be a close one! Roll an athletics check to get into the fireplace and an exploding d6 for the barrel of oil.
>
>**Grindon**: Okay that's... 1d20+4 then... d6!
>
>*GNOLL*: [18]
>
>*GNOLL*: [25]
>
>**GM**: The explosion blasts behind you as you dive inside. You still take 4 damage as you smash into the stone and your ears ring as the barrel bursts, evaporating the gnoll.
>
>**Grindon The Brave**: Ouch!
>
>**GM**: I'm pretty sure whatever else is in this cave heard that too :)


## Traditional Explosions

When a dice is marked as Exploding ("!"), if it rolls its maximum value, we will reroll it one again and add the result. If it keeps hitting the max value, we keep rolling.

> Note: If you want to only re-roll once, look at "Rerolling" below instead.

### Multiple Explosions

*Under Construction*

Note: if you explode multiple dice, they will be grouped together as a condition for explosion:

```2d3! -> Explodes on (3)(3)```

If you want to explode them individually try:

```d3! + d3! -> Explodes on (3) and Explodes on (3)```

## Penetrating Explosions

*Under Construction*

When an explosion is set off, the range of the next dice is reduced by 1 step. As we don't want to encode any system specific mechanics here, the 'steps' of dice need to be specified.

> {d4,d6,d8,d10,d12,d20}!p

Not Implemented Yet. See [Issue #11](https://github.com/ianfhunter/GNOLL/issues/11)

Due to the more complicated notation, and the likelyhood that a penetrating explosion is standard across an rpg system, we recommend saving these rolls as macros.


## Diminishing Explosions

Diminishing Explosions can be thought of the reverse of Penetrating Explosions. When an explosion is set off, we roll a smaller dice each time.

GNOLL will implement this through the same syntax as Penetrating Explosions.

## Imploding dice

*Under Construction*

There is no consistent standard for imploding dice. Here are a few candidates:
- [Inverse Explosion - Rerolling when not matching your number](https://www.welshpiper.com/imploding-dice/)
- [Negative Explosion](http://www.firehawkgames.biz/?qa_faqs=what-is-an-imploding-dice-roll)

### Inverse Explosion

This seems an unlikely use case as it involves many rolls, and at a tabletop that's not realistic. If there is found to be a genuine requirement for this feature from a well known game we may reconsider it within the scope of GNOLL.

### Negative Explosion

The notation for negative explosions is often "~" instead of "!" (Citation Needed!). It activates on the lowest number match rather than the highest. The rerolled values are subtracted from the total.

It is also yet to be determined if there are any real use cases of this notation style.
