---
title: Math with Dice
published: true
nav_order: 4
---

# Math with Dice

{: .story }   
>   GM: As you climb out of the fireplace, roll a stealth check to avoid making noise in the charcoal and debris below.
>
>   Gridon: 1d20+4
>
>   GNOLL: [5]
>
>   GM: Oh no! A big hairy gnoll in the next room has noticed all the noise you're making!
>
>   Gridon: Crap! I make a run for it. Where's the door?
>
>   GM: There's another door, but... it's locked!

## Numeric Dice
For Numeric Dice, math follows normal conventions.
 - Add (+): 
   - 1+2 = 3
 - Subtract (-): 
   - 4-3 = 1
 - Multiply (*): 
   - 5*2: 10
 - Divide (rounding up(\\) and rounding down(/)): 
   - 10/2: 5
 - Modulo (%): 
   - 10%3 = 1
 - Brackets (())

{: .warning }
Be careful with characters like \ and / and be sure to escape them if needed in your calling program.

## Symbolic Dice
For Symbolic Dice, even if the symbols are numbers, the logic is different as GNOLL treats the values as strings (words).

- Add (+) Concatenate two symbols: "A"+"B" = "AB"
- Subtract (-) Remove if there is overlap between symbols: 
   - "AAA"-"C"= "AAA".  
   - "ABA"-"A"= "BA"
- Multiply (*) - Duplicate if multiplying by a number. Cannot multiply by a symbol
   - "A" * 5 = "AAAAA"
   - "A" * "B" = ERR
- Divide (\\ or /): Currently always produces an error.
- Modulo (%): Currently always produces an error.
- Brackets (())

  

   
