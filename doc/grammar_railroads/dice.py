Diagram(
    Choice(
        0,
        Sequence(
                Group(
                Optional('<INT>', 'skip'), 
                "Number of Dice"
            ),
            Sequence('d'),
            Choice(
                0, 
                Group("NUMBER", "regular sided die"),
                Group("f", "Fate Die"),
                Group(
                    Sequence(
                        '{', 
                        '<INT>', 
                        ZeroOrMore(
                            Choice(0, 
                                ", <INT>", 
                                ", <INT>..<INT>"
                            )
                        ), 
                        '}'
                    ),
                    "Manual Numeric Collection"
                ),
                Group(
                    Sequence('{', '<INT>', ZeroOrMore(Choice(0, ", <string>", ", <string>..<string>")), '}'),
                    "Symbolic Die"
                ),
                Group(
                    Sequence(
                    "@", "<string(key)>"
                    ),
                    "Macro Lookup"
                )
            ),
        ),
        Group(
            Sequence("<int>"),
            "Just a Number"
        )
    )
)