---
title: Built-In Macros
published: true
parent: Dice Notation
nav_order: 9
---

# Built-In Macros

{: .story }
>**GM**: You fail to secure yourself on the wall and slip towards the spikes. While falling, you hit your head against the wall.
>
>**Grindon**: Gosh, that hurts.
>
>**GM**: You miraculously hit the ground without dying. But your blow to the head makes you delirious.
>
>**Grindon**: Oh look, fairies wearing armor painted with Zodiac signs!
>
>**GM**: Yes... (sigh) As they fly around your head, you decide to eat one of them.
>
>**Grindon**: Okay that's a @PLANETS die?
>
>*GNOLL*: [Mars]
>
>**Grindon The Brave**: Well... That's not my favorite flavour...
>
>**GM**: Crunchy! At least you didn't have to roll a dice that had a 1! That would have been a disaster!


## Supported Macros

Here are a sample of the dice that can be used via Macro Accessors

| Dice Type | Possible Values | Macro Accessor |
| ----------- | -------------- | --------------- |
| Poker Dice | 9, 10, J, K, Q, A | @POKER_DICE |
| Chess Dice | Pawn, Knight, Bishop, Rook, Queen, and King | @CHESS_DICE |
| Directions | NORTH, SOUTH, WEST, EAST | @DIRECTION_D4 |
| Card Suits| CLUBS, DIAMONDS, HEARTS, SPADES | @CARD_SUIT |
| Zodiac | Aries through Pisces | @ZODIAC |
| Planets | Sun, Moon, all the planets from Mercury all the way to Pluto, Ascending Node, Descending Node | @PLANETS |

More can be found in the `builtins/` folder [here](https://github.com/ianfhunter/GNOLL/tree/main/builtins)

## Usage

To use a Macro, access it with '@' as below
> @POKER_DICE
