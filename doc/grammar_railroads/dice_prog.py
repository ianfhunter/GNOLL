Diagram(
   Sequence(
        Group(ZeroOrMore(
            Sequence(
                "#", 
                "<string(key)>",
                "=", NonTerminal("mathOp"),
                ";"
            )
        ),"Macro Creation"),
        NonTerminal("mathOp")

   )
)