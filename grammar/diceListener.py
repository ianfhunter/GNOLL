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


    # Enter a parse tree produced by diceParser#Add.
    def enterAdd(self, ctx:diceParser.AddContext):
        pass

    # Exit a parse tree produced by diceParser#Add.
    def exitAdd(self, ctx:diceParser.AddContext):
        pass


    # Enter a parse tree produced by diceParser#Sub.
    def enterSub(self, ctx:diceParser.SubContext):
        pass

    # Exit a parse tree produced by diceParser#Sub.
    def exitSub(self, ctx:diceParser.SubContext):
        pass


    # Enter a parse tree produced by diceParser#BubbleMulDiv.
    def enterBubbleMulDiv(self, ctx:diceParser.BubbleMulDivContext):
        pass

    # Exit a parse tree produced by diceParser#BubbleMulDiv.
    def exitBubbleMulDiv(self, ctx:diceParser.BubbleMulDivContext):
        pass


    # Enter a parse tree produced by diceParser#BubblePow.
    def enterBubblePow(self, ctx:diceParser.BubblePowContext):
        pass

    # Exit a parse tree produced by diceParser#BubblePow.
    def exitBubblePow(self, ctx:diceParser.BubblePowContext):
        pass


    # Enter a parse tree produced by diceParser#DivUp.
    def enterDivUp(self, ctx:diceParser.DivUpContext):
        pass

    # Exit a parse tree produced by diceParser#DivUp.
    def exitDivUp(self, ctx:diceParser.DivUpContext):
        pass


    # Enter a parse tree produced by diceParser#Mul.
    def enterMul(self, ctx:diceParser.MulContext):
        pass

    # Exit a parse tree produced by diceParser#Mul.
    def exitMul(self, ctx:diceParser.MulContext):
        pass


    # Enter a parse tree produced by diceParser#DivDown.
    def enterDivDown(self, ctx:diceParser.DivDownContext):
        pass

    # Exit a parse tree produced by diceParser#DivDown.
    def exitDivDown(self, ctx:diceParser.DivDownContext):
        pass


    # Enter a parse tree produced by diceParser#BubbleNeg.
    def enterBubbleNeg(self, ctx:diceParser.BubbleNegContext):
        pass

    # Exit a parse tree produced by diceParser#BubbleNeg.
    def exitBubbleNeg(self, ctx:diceParser.BubbleNegContext):
        pass


    # Enter a parse tree produced by diceParser#Power.
    def enterPower(self, ctx:diceParser.PowerContext):
        pass

    # Exit a parse tree produced by diceParser#Power.
    def exitPower(self, ctx:diceParser.PowerContext):
        pass


    # Enter a parse tree produced by diceParser#Negate.
    def enterNegate(self, ctx:diceParser.NegateContext):
        pass

    # Exit a parse tree produced by diceParser#Negate.
    def exitNegate(self, ctx:diceParser.NegateContext):
        pass


    # Enter a parse tree produced by diceParser#NoNegate.
    def enterNoNegate(self, ctx:diceParser.NoNegateContext):
        pass

    # Exit a parse tree produced by diceParser#NoNegate.
    def exitNoNegate(self, ctx:diceParser.NoNegateContext):
        pass


    # Enter a parse tree produced by diceParser#Value.
    def enterValue(self, ctx:diceParser.ValueContext):
        pass

    # Exit a parse tree produced by diceParser#Value.
    def exitValue(self, ctx:diceParser.ValueContext):
        pass


    # Enter a parse tree produced by diceParser#Brackets.
    def enterBrackets(self, ctx:diceParser.BracketsContext):
        pass

    # Exit a parse tree produced by diceParser#Brackets.
    def exitBrackets(self, ctx:diceParser.BracketsContext):
        pass


    # Enter a parse tree produced by diceParser#die_roll.
    def enterDie_roll(self, ctx:diceParser.Die_rollContext):
        pass

    # Exit a parse tree produced by diceParser#die_roll.
    def exitDie_roll(self, ctx:diceParser.Die_rollContext):
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


