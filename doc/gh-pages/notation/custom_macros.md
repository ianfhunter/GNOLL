---
title: Custom Macros
published: true
nav_order: 10
parent: Dice Notation
---

# Custom Macros

{: .story }
>**GM**: You wake up from your dream, finding an old creature resembling a witch. Seeing your bleeding head, it offers you to choose a potion.
>
>**Grindon**: Can I pick the healing potion?
>
>**GM**: Almost. There is one bright-green healing potion. There is also one deep-red deadly potion, that would also help with your bleeding head, but not with your quest. And finally an intriguing blue potion, full of sprinkles swirling inside the bottle.
>
>**Grindon**: Ok. How do I pick one?
>
>**GM**: Extreme solutions like this one require special die. This one is a Please-Save-Me die, with 3 faces named "life", "death" and "something else".
>
>**Grindon**: Okay! Com'on die.
>
>*GNOLL*: [SOMETHING_ELSE]
>
>**Grindon The Brave**: Uhoh.. I am starting to feel weird...

## Usage

*This is an advanced feature. Feel free to ask us for help!*

There are certain system-specific [Built-In Macros](https://github.com/ianfhunter/GNOLL/tree/main/builtins) for you to take advantage of.

Before rolling your dice, you can define some macros

All strings (words) must be capitalized. This is to avoid confusion with the rest of the dice notation

`$EVENSIX= {2,4,6,8,10,12}`

You can use ranges

`$DTWENTYBONUS = {1..20, 30}`

You can also use words

`$FRIENDS={JOHN,MARY,TAI}`

**Note:** Currently, if you wish to roll stored dice multiple times, you must do this in seperate statements e.g. `@FRIENDS;@FRIENDS;@FRIENDS`