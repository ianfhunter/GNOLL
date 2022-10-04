---
title: Conditions & Filters
published: true
nav_order: 11
---

# Conditions & Filters

{: .story }   
>TODO

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

**Example: **

4𝑑6𝑓 < 3 = 𝑓𝑖𝑙𝑡𝑒𝑟({4,1,2,5}, ” < 3”) = {2,1} 

## Combination with other operations

Filters can be powerful when combined with other operations. Such as rerolling when certain criteria are met.

*Under Construction. Examples to be added*
