---
title: Symbolic Dice
published: true
nav_order: 2
parent: Dice Notation
---

# Symbolic Dice

{: .story}
>
>**Grindon**: Hmm, I don't fancy getting in a brawl before I even enter the dungeon. And they might sound an alarm. I'll take a moment to look around for an alternate entrance.
>
>**GM**: Okay, Roll a Fate die and let's see
>
>**Grindon** the Brave: C'mon dice, work with me here! "d{-,0,+}"!
>
>*GNOLL*: ["+"]
>
>**Grindon the Brave**: Yes!
>
>**GM**: Sure enough, it seems like there's some sort of chimney hole about 20ft up from the main entrance. It looks big enough to squeeze through.


Symbolic dice have symbols on their sides instead of numbers. These could be letters, shapes or other iconography.

To specify a symbolic dice, the symbols must be listed as there's no way for the parser to know what comes next. This syntax is very similar to custom numeric ranges. A simple example is d{A,B,C,D}.

Some operations work differently on Symbolic Dice than on Numeric Dice as they do not inherently have a value associated with them. For example numeric values of 1+1 would give a result of 2, but with symbolic dice A+A the result is AA. More of these differences are discussed in the operation descriptions themselves.

All symbolic dice **must** be capitalized, so as not to conflict with other dice notation terms.

{: .explanation}
> There are several overlaps in notation that cannot be distinguished from one another usually.
>
> One example is a d66, which usually is a 66-sided die, but in some systems one d6 represents the tens digit, and the other the single digit (Meaning that values like 60 cannot be represented). Our solution is to keep traditional notation in lowercase and allow overlapping logic to share names, but captialized (d66 vs D66).
