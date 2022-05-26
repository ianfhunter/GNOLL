Diagram(
  Choice(0,
    NonTerminal('<Dice>'),
    Group(
       Sequence(
           NonTerminal('<DiceOp>'),
          'r',
           Choice(0, 'r', NonTerminal('<condition>'))
        ),
        "Rerolling"
      ),
     Group(
       Sequence(
           NonTerminal('<DiceOp>'),
          '!',
           Optional(Choice(0, 'o', 'p'))
        ),
        "Explosion"
     ),
     Group(
       Sequence(

           NonTerminal('<DiceOp>*'),
           Choice(0, 'k', 'd'),
           Choice(0, 'h', 'l')
        ),
        "Drop/Keep"
     ),
     Group(
       Sequence(
           NonTerminal('<DiceOp>'),
           'f',
           NonTerminal('<condition>'),
        ),
        "Filter"
     ),
     Group(
       Sequence(
           NonTerminal('<DiceOp>'),
           'c',
        ),
        "Count"
     ),
     Group(
        Sequence(
            NonTerminal('<DiceOp>'),
           'u',
        ),
        "Unique"
     ),
   ),
)