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


    # Enter a parse tree produced by diceParser#assignment.
    def enterAssignment(self, ctx:diceParser.AssignmentContext):
        pass

    # Exit a parse tree produced by diceParser#assignment.
    def exitAssignment(self, ctx:diceParser.AssignmentContext):
        pass


    # Enter a parse tree produced by diceParser#variable.
    def enterVariable(self, ctx:diceParser.VariableContext):
        pass

    # Exit a parse tree produced by diceParser#variable.
    def exitVariable(self, ctx:diceParser.VariableContext):
        pass


    # Enter a parse tree produced by diceParser#sequence.
    def enterSequence(self, ctx:diceParser.SequenceContext):
        pass

    # Exit a parse tree produced by diceParser#sequence.
    def exitSequence(self, ctx:diceParser.SequenceContext):
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


    # Enter a parse tree produced by diceParser#DivUp.
    def enterDivUp(self, ctx:diceParser.DivUpContext):
        pass

    # Exit a parse tree produced by diceParser#DivUp.
    def exitDivUp(self, ctx:diceParser.DivUpContext):
        pass


    # Enter a parse tree produced by diceParser#BubbleSeveral.
    def enterBubbleSeveral(self, ctx:diceParser.BubbleSeveralContext):
        pass

    # Exit a parse tree produced by diceParser#BubbleSeveral.
    def exitBubbleSeveral(self, ctx:diceParser.BubbleSeveralContext):
        pass


    # Enter a parse tree produced by diceParser#Mul.
    def enterMul(self, ctx:diceParser.MulContext):
        pass

    # Exit a parse tree produced by diceParser#Mul.
    def exitMul(self, ctx:diceParser.MulContext):
        pass


    # Enter a parse tree produced by diceParser#Modulo.
    def enterModulo(self, ctx:diceParser.ModuloContext):
        pass

    # Exit a parse tree produced by diceParser#Modulo.
    def exitModulo(self, ctx:diceParser.ModuloContext):
        pass


    # Enter a parse tree produced by diceParser#DivDown.
    def enterDivDown(self, ctx:diceParser.DivDownContext):
        pass

    # Exit a parse tree produced by diceParser#DivDown.
    def exitDivDown(self, ctx:diceParser.DivDownContext):
        pass


    # Enter a parse tree produced by diceParser#BubblePow.
    def enterBubblePow(self, ctx:diceParser.BubblePowContext):
        pass

    # Exit a parse tree produced by diceParser#BubblePow.
    def exitBubblePow(self, ctx:diceParser.BubblePowContext):
        pass


    # Enter a parse tree produced by diceParser#Several.
    def enterSeveral(self, ctx:diceParser.SeveralContext):
        pass

    # Exit a parse tree produced by diceParser#Several.
    def exitSeveral(self, ctx:diceParser.SeveralContext):
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


    # Enter a parse tree produced by diceParser#die_modifier.
    def enterDie_modifier(self, ctx:diceParser.Die_modifierContext):
        pass

    # Exit a parse tree produced by diceParser#die_modifier.
    def exitDie_modifier(self, ctx:diceParser.Die_modifierContext):
        pass


    # Enter a parse tree produced by diceParser#count.
    def enterCount(self, ctx:diceParser.CountContext):
        pass

    # Exit a parse tree produced by diceParser#count.
    def exitCount(self, ctx:diceParser.CountContext):
        pass


    # Enter a parse tree produced by diceParser#bang.
    def enterBang(self, ctx:diceParser.BangContext):
        pass

    # Exit a parse tree produced by diceParser#bang.
    def exitBang(self, ctx:diceParser.BangContext):
        pass


    # Enter a parse tree produced by diceParser#explode.
    def enterExplode(self, ctx:diceParser.ExplodeContext):
        pass

    # Exit a parse tree produced by diceParser#explode.
    def exitExplode(self, ctx:diceParser.ExplodeContext):
        pass


    # Enter a parse tree produced by diceParser#implode.
    def enterImplode(self, ctx:diceParser.ImplodeContext):
        pass

    # Exit a parse tree produced by diceParser#implode.
    def exitImplode(self, ctx:diceParser.ImplodeContext):
        pass


    # Enter a parse tree produced by diceParser#force.
    def enterForce(self, ctx:diceParser.ForceContext):
        pass

    # Exit a parse tree produced by diceParser#force.
    def exitForce(self, ctx:diceParser.ForceContext):
        pass


    # Enter a parse tree produced by diceParser#exactMatch.
    def enterExactMatch(self, ctx:diceParser.ExactMatchContext):
        pass

    # Exit a parse tree produced by diceParser#exactMatch.
    def exitExactMatch(self, ctx:diceParser.ExactMatchContext):
        pass


    # Enter a parse tree produced by diceParser#lessOrEqualTo.
    def enterLessOrEqualTo(self, ctx:diceParser.LessOrEqualToContext):
        pass

    # Exit a parse tree produced by diceParser#lessOrEqualTo.
    def exitLessOrEqualTo(self, ctx:diceParser.LessOrEqualToContext):
        pass


    # Enter a parse tree produced by diceParser#greaterOrEqualTo.
    def enterGreaterOrEqualTo(self, ctx:diceParser.GreaterOrEqualToContext):
        pass

    # Exit a parse tree produced by diceParser#greaterOrEqualTo.
    def exitGreaterOrEqualTo(self, ctx:diceParser.GreaterOrEqualToContext):
        pass


    # Enter a parse tree produced by diceParser#lessThan.
    def enterLessThan(self, ctx:diceParser.LessThanContext):
        pass

    # Exit a parse tree produced by diceParser#lessThan.
    def exitLessThan(self, ctx:diceParser.LessThanContext):
        pass


    # Enter a parse tree produced by diceParser#greaterThan.
    def enterGreaterThan(self, ctx:diceParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by diceParser#greaterThan.
    def exitGreaterThan(self, ctx:diceParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by diceParser#reroll.
    def enterReroll(self, ctx:diceParser.RerollContext):
        pass

    # Exit a parse tree produced by diceParser#reroll.
    def exitReroll(self, ctx:diceParser.RerollContext):
        pass


    # Enter a parse tree produced by diceParser#rr_times.
    def enterRr_times(self, ctx:diceParser.Rr_timesContext):
        pass

    # Exit a parse tree produced by diceParser#rr_times.
    def exitRr_times(self, ctx:diceParser.Rr_timesContext):
        pass


    # Enter a parse tree produced by diceParser#rr_all.
    def enterRr_all(self, ctx:diceParser.Rr_allContext):
        pass

    # Exit a parse tree produced by diceParser#rr_all.
    def exitRr_all(self, ctx:diceParser.Rr_allContext):
        pass


    # Enter a parse tree produced by diceParser#subset.
    def enterSubset(self, ctx:diceParser.SubsetContext):
        pass

    # Exit a parse tree produced by diceParser#subset.
    def exitSubset(self, ctx:diceParser.SubsetContext):
        pass


    # Enter a parse tree produced by diceParser#LowerSN.
    def enterLowerSN(self, ctx:diceParser.LowerSNContext):
        pass

    # Exit a parse tree produced by diceParser#LowerSN.
    def exitLowerSN(self, ctx:diceParser.LowerSNContext):
        pass


    # Enter a parse tree produced by diceParser#HigherSN.
    def enterHigherSN(self, ctx:diceParser.HigherSNContext):
        pass

    # Exit a parse tree produced by diceParser#HigherSN.
    def exitHigherSN(self, ctx:diceParser.HigherSNContext):
        pass


    # Enter a parse tree produced by diceParser#LowerRN.
    def enterLowerRN(self, ctx:diceParser.LowerRNContext):
        pass

    # Exit a parse tree produced by diceParser#LowerRN.
    def exitLowerRN(self, ctx:diceParser.LowerRNContext):
        pass


    # Enter a parse tree produced by diceParser#HigherRN.
    def enterHigherRN(self, ctx:diceParser.HigherRNContext):
        pass

    # Exit a parse tree produced by diceParser#HigherRN.
    def exitHigherRN(self, ctx:diceParser.HigherRNContext):
        pass


    # Enter a parse tree produced by diceParser#LowerRND.
    def enterLowerRND(self, ctx:diceParser.LowerRNDContext):
        pass

    # Exit a parse tree produced by diceParser#LowerRND.
    def exitLowerRND(self, ctx:diceParser.LowerRNDContext):
        pass


    # Enter a parse tree produced by diceParser#HigherRND.
    def enterHigherRND(self, ctx:diceParser.HigherRNDContext):
        pass

    # Exit a parse tree produced by diceParser#HigherRND.
    def exitHigherRND(self, ctx:diceParser.HigherRNDContext):
        pass


    # Enter a parse tree produced by diceParser#subset_size.
    def enterSubset_size(self, ctx:diceParser.Subset_sizeContext):
        pass

    # Exit a parse tree produced by diceParser#subset_size.
    def exitSubset_size(self, ctx:diceParser.Subset_sizeContext):
        pass


    # Enter a parse tree produced by diceParser#amount.
    def enterAmount(self, ctx:diceParser.AmountContext):
        pass

    # Exit a parse tree produced by diceParser#amount.
    def exitAmount(self, ctx:diceParser.AmountContext):
        pass


    # Enter a parse tree produced by diceParser#StandardFace.
    def enterStandardFace(self, ctx:diceParser.StandardFaceContext):
        pass

    # Exit a parse tree produced by diceParser#StandardFace.
    def exitStandardFace(self, ctx:diceParser.StandardFaceContext):
        pass


    # Enter a parse tree produced by diceParser#CustomFace.
    def enterCustomFace(self, ctx:diceParser.CustomFaceContext):
        pass

    # Exit a parse tree produced by diceParser#CustomFace.
    def exitCustomFace(self, ctx:diceParser.CustomFaceContext):
        pass


    # Enter a parse tree produced by diceParser#numeric_sequence.
    def enterNumeric_sequence(self, ctx:diceParser.Numeric_sequenceContext):
        pass

    # Exit a parse tree produced by diceParser#numeric_sequence.
    def exitNumeric_sequence(self, ctx:diceParser.Numeric_sequenceContext):
        pass


    # Enter a parse tree produced by diceParser#numeric_item.
    def enterNumeric_item(self, ctx:diceParser.Numeric_itemContext):
        pass

    # Exit a parse tree produced by diceParser#numeric_item.
    def exitNumeric_item(self, ctx:diceParser.Numeric_itemContext):
        pass


    # Enter a parse tree produced by diceParser#seq_item.
    def enterSeq_item(self, ctx:diceParser.Seq_itemContext):
        pass

    # Exit a parse tree produced by diceParser#seq_item.
    def exitSeq_item(self, ctx:diceParser.Seq_itemContext):
        pass


    # Enter a parse tree produced by diceParser#die.
    def enterDie(self, ctx:diceParser.DieContext):
        pass

    # Exit a parse tree produced by diceParser#die.
    def exitDie(self, ctx:diceParser.DieContext):
        pass


    # Enter a parse tree produced by diceParser#fateDie.
    def enterFateDie(self, ctx:diceParser.FateDieContext):
        pass

    # Exit a parse tree produced by diceParser#fateDie.
    def exitFateDie(self, ctx:diceParser.FateDieContext):
        pass


