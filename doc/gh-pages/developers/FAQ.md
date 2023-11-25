---
title: FAQs
published: true
nav_order: 14
parent: Technical Information
---

# FAQ

Have a Feature Request? [File it for us to look at](https://github.com/ianfhunter/GNOLL/issues). We also have a place for [Discussion](https://github.com/ianfhunter/GNOLL/discussions).

{: .question }
> How can I use unicode, emojis and other strange characters in GNOLL?

GNOLL does not support special characters natively, due to limitations of dependant libraries and significant additional complexity. Our recommendation is to use a representative string for these characters. e.g. 🐺 could be input to GNOLL as WOLF.

{: .question }
> How can I use GNOLL to draw cards out of a deck?

GNOLL does not support tracking the state of internal counters between executions and/or statements, so cannot remove cards from a pool. We recommend passing reduced options to GNOLL from your script as cards/dice sides are revealed.

e.g.
> roll("d{TEN, JACK, QUEEN, KING, ACE}")
> result: JACK
>
> roll("d{TEN, QUEEN, KING, ACE}")
> result: QUEEN

{: .question }
> GNOLL uses a slightly different syntax than what I would like

While we have put a lot of thought into GNOLL's choices of characters, You may change which characters are used for operations in the [dice.lex](https://github.com/ianfhunter/GNOLL/blob/main/src/grammar/dice.lex) file.

For example, to allow using the full word 'reroll' instead of the shorthand 'r' you would make this change:
```lex
// old
[r] {
    return(REROLL);
}
// new
[r|reroll] {
    return(REROLL);
}
```
Note you will need to manage conflicts in grammar yourself. (e.g. if you wanted to use the 'x' symbol for multiplication, you would need to also find a new symbol for the `REPEAT` token.
For more complicated statements you will need to become familiar with [Regular Expressions](https://en.m.wikipedia.org/wiki/Regular_expression)


{: .question }
> GNOLL produces an overall result, but I need to know what each dice value was!

This is possible! Just enable introspection or "dice breakdown" and you'll get the individual results as well as the final ones.
This can be enabled via a parameter to the [main GNOLL roll function](https://www.ianhunter.ie/GNOLL/developers/installation.html).

<!-- either via a command line switch (where available) or as -->

{: .question }
> I wish to cite GNOLL. What is the most appropriate item to use?

Please cite one of our publications. Feel free to [raise an issue](https://github.com/ianfhunter/GNOLL/issues) if you are not sure.
- [GNOLL: Efficient Multi-Lingual Software for Real-World Dice Notation and Extensions](https://joss.theoj.org/papers/c704c5148e622d32403948320c5e96a1)
- [Application of the Central Limit Theorem to dice notation parsing](https://beta.briefideas.org/ideas/fc25de499b44d47685188df4d09e144f)
