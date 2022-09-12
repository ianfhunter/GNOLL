---
title: Built-In Macros
published: true

nav_order: 9
---
<!-- TODO: Grindon's Tale -->

Here are a sample of the dice that can be used via Macro Accessors

<!-- textlint-disable -->
<!-- Ignore Suggestion for Node to be named Node.js -->

| Dice Type | Possible Values | Macro Accessor | 
| --------- | --------------- | -------------- |
| Poker Dice | 9, 10, J, K, Q, A | #POKER_DICE |
| Chess Dice | Pawn, Knight, Bishop, Rook, Queen, and King | #CHESS_DICE |
| Directions | NORTH, SOUTH, WEST, EAST | #DIRECTION_D4 |
| Card Suits| CLUBS, DIAMONDS, HEARTS, SPADES | #CARD_SUIT |
| Zodiac | Aries through Pisces | #ZODIAC |
| Planets | Sun, Moon, Mercury through Pluto, Ascending Node, and Descending Node | #PLANETS |


<!-- textlint-enable -->

More can be found in the `builtins/` folder [here](https://github.com/ianfhunter/GNOLL/tree/main/builtins)

To use a Macro, access it with '#' as below
> #POKER_DICE
