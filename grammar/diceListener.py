# Generated from dice.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .diceParser import diceParser
else:
    from diceParser import diceParser

# This class defines a complete listener for a parse tree produced by diceParser.
class diceListener(ParseTreeListener):

    # Enter a parse tree produced by diceParser#schema.
    def enterSchema(self, ctx:diceParser.SchemaContext):
        pass

    # Exit a parse tree produced by diceParser#schema.
    def exitSchema(self, ctx:diceParser.SchemaContext):
        pass


    # Enter a parse tree produced by diceParser#dice_roll.
    def enterDice_roll(self, ctx:diceParser.Dice_rollContext):
        pass

    # Exit a parse tree produced by diceParser#dice_roll.
    def exitDice_roll(self, ctx:diceParser.Dice_rollContext):
        pass


    # Enter a parse tree produced by diceParser#die_roll.
    def enterDie_roll(self, ctx:diceParser.Die_rollContext):
        pass

    # Exit a parse tree produced by diceParser#die_roll.
    def exitDie_roll(self, ctx:diceParser.Die_rollContext):
        pass


    # Enter a parse tree produced by diceParser#die.
    def enterDie(self, ctx:diceParser.DieContext):
        pass

    # Exit a parse tree produced by diceParser#die.
    def exitDie(self, ctx:diceParser.DieContext):
        pass


    # Enter a parse tree produced by diceParser#subset.
    def enterSubset(self, ctx:diceParser.SubsetContext):
        pass

    # Exit a parse tree produced by diceParser#subset.
    def exitSubset(self, ctx:diceParser.SubsetContext):
        pass


    # Enter a parse tree produced by diceParser#highest.
    def enterHighest(self, ctx:diceParser.HighestContext):
        pass

    # Exit a parse tree produced by diceParser#highest.
    def exitHighest(self, ctx:diceParser.HighestContext):
        pass


    # Enter a parse tree produced by diceParser#lowest.
    def enterLowest(self, ctx:diceParser.LowestContext):
        pass

    # Exit a parse tree produced by diceParser#lowest.
    def exitLowest(self, ctx:diceParser.LowestContext):
        pass


    # Enter a parse tree produced by diceParser#amount.
    def enterAmount(self, ctx:diceParser.AmountContext):
        pass

    # Exit a parse tree produced by diceParser#amount.
    def exitAmount(self, ctx:diceParser.AmountContext):
        pass


    # Enter a parse tree produced by diceParser#faces.
    def enterFaces(self, ctx:diceParser.FacesContext):
        pass

    # Exit a parse tree produced by diceParser#faces.
    def exitFaces(self, ctx:diceParser.FacesContext):
        pass


