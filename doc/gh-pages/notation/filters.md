---
title: Conditions & Filters
published: true
nav_order: 11
---

# Conditions & Filters

{: .story }
>**GM**: You are lucky. The potion saved your life, cured all your wounds and gaved you an extra boost of energy. As you get up, you realize that you are in a room filled with bags of golden coins.
>
>**Grindon**: The heart of the dunjeon!..
>
>**GM**: Yes. Before anyone appear and catch you, you grab as many bags you can in your arms.
>
>**Grindon**: Finally, all this time training in the woods will serve me well. I surely can hold 8 of those nice bags. Let's roll 8d20.
>
>**GM**: True but hold on. The bags are slippery. And small bags containing 4 coins or less may fall from your arms.
>
>**Grindon**: Okay, let's roll. Please dice, be kind.
>
>*GNOLL*: [{16, 1, 5, 8, 1, 9, 1, 13}]
>
>**GM**: You escape the dunjeon with...
>
>**Grindon The Brave**: Not so fast, dear GM. I see lots of 1s here. It is time for my special class feature. I knew it would come handy.
>
> *GNOLL*: [{2, 4, 3}]
>
>**GM**: Lucky you, you did not get 1s in your rerolls.
>
>**Grindon The Brave**: I suppose we can say so...

# Filtering

In many games, certain logic is only required if a particular value is rolled. For example, the board game One Deck Dungeon [5] contains a scenario
that requires the player to discard any 2s rolled in their roll. Conditional statements allow a high range of flexibility for
cases such as these.

When applied to a vector of rolls, a conditional can act as a filter to remove rolls that do not satisfy the criteria.
Conditionals in GNOLL operations take the same form as one might find in typical programming languages.

| Symbol | Meaning      |
| ------ | ------------ |
|   ==   | Equal To     |
|   !=   | Not Equal To     |
|   <    | Less Than    |
|   >    | Greater Than |
|   <=   | Less Than OR Equal To     |
|   >=   | Greater Than OR Equal To     |

Filters use conditionals to remove dice rolls that do not match the conditional check. Equation 16 shows four dice
being rolled and then two of them discarded for not matching the filter criteria.

**Example:**

4𝑑6𝑓 < 3 = 𝑓𝑖𝑙𝑡𝑒𝑟({4,1,2,5}, ” < 3”) = {2,1}

## Combination with other operations

Filters can be powerful when combined with other operations. Such as rerolling when certain criteria are met.

*Under Construction. Examples to be added*
