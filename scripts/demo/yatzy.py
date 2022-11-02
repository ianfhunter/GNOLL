import importlib.util as iu
import os
import sys
from collections import Counter

# Copy-Pasted from test/util.py. Real app would just import gnoll from pypi
SRC_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../src/python/code/gnoll/")
)
m = os.path.join(SRC_DIR, "parser.py")
spec = iu.spec_from_file_location("dt", m)
dt = iu.module_from_spec(spec)
spec.loader.exec_module(dt)

roll = dt.roll


def is_low_straight(dice):
    """1-5 continuous"""
    return 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice


def is_high_straight(dice):
    """2-6 continuous"""
    return 6 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice


def show_individual_dice_score(top):
    """Print out pip scores"""
    print(
        f"""
[1]: {top[0]}
[2]: {top[1]}
[3]: {top[2]}
[4]: {top[3]}
[5]: {top[4]}
[6]: {top[5]}"""
    )


def scorecard(dice):
    """Print out player scorecard"""
    one_pair_sum = 0
    two_pair_sum = 0
    three_oak_sum = 0
    four_oak_sum = 0
    low_straight = 0
    high_straight = 0
    full_house = 0
    chance = 0
    five_oak = 0
    top_bonus = 0

    def tot_sides(y, dice):
        return sum([x for x in dice if x == y])

    def count_sides(v, dice):
        return [a for a, b in Counter(dice).items() if b == v]

    top = [
        tot_sides(1, dice),
        tot_sides(2, dice),
        tot_sides(3, dice),
        tot_sides(4, dice),
        tot_sides(5, dice),
        tot_sides(6, dice),
    ]

    top_bonus = 50 if sum(top) >= 63 else 0

    fiveoak = count_sides(5, dice)
    foak = count_sides(4, dice)
    toak = count_sides(3, dice)
    twoak = count_sides(2, dice)

    if len(fiveoak) > 0:
        five_oak = 50
    elif len(foak) > 0:
        four_oak_sum = foak[0] * 4
    elif len(toak) > 0:
        if len(twoak) > 0:
            # full house
            full_house = toak[0] * 3 + twoak[0] * 2
        else:
            three_oak_sum = toak[0] * 3
    elif len(twoak) > 0:
        if len(twoak) == 2:
            two_pair_sum = twoak[0] * 2 + twoak[1] * 2
        else:
            one_pair_sum = twoak[0] * 2
    elif is_low_straight(dice):
        low_straight = 15
    elif is_high_straight(dice):
        low_straight = 20
    else:
        chance = sum(dice)

    total = sum(
        [
            top_bonus,
            one_pair_sum,
            two_pair_sum,
            three_oak_sum,
            four_oak_sum,
            low_straight,
            high_straight,
            full_house,
            chance,
            five_oak,
        ]
    )

    print(f"Dice: {dice}")
    show_individual_dice_score(top)

    print(
        f"""

Top Bonus: {top_bonus}

One Pair: {one_pair_sum}
Two Pairs: {two_pair_sum}
Three of a Kind: {three_oak_sum}
Four of a Kind: {four_oak_sum}
Small Straight: {low_straight}
Large Straight: {high_straight}
Full House: {full_house}
Chance: {chance}
Yatzy: {five_oak}

Total: {total}
    """
    )
    return total


def yatzy_round(dice, first=False):
    """Roll Yatzy Dice and replace if nessicary"""
    if first:
        _, dice = roll("d6;d6;d6;d6;d6")
    else:
        choice = ""
        while choice.upper() not in ["R", "K"]:
            choice = input("(K)eep or (R)oll again?")

        if choice.upper() == "K":
            print("Thank you for playing")
            sys.exit(0)

        # Roll 2
        print(
            f"""
        1: {dice[0]}
        2: {dice[1]}
        3: {dice[2]}
        4: {dice[3]}
        5: {dice[4]}
        """
        )
        # TODO: Check valid input
        choice = input(
            "Please enter the numbers you wish to swap (space seperated)")
        choice = sorted([int(x) for x in choice.split(" ")], reverse=True)
        for x in choice:
            del dice[x - 1]

        print("Remaining Dice:", dice)

        new_dice_roll = "d6;" * len(choice)
        _, second_roll = roll(new_dice_roll)
        print("New Dice Roll: ", second_roll)

        dice.extend(second_roll)
        print("Joined Dice:", dice)

    scorecard(dice)

    return dice


def main():
    """Play a game of Yatzy"""
    # Roll 1.
    dice = yatzy_round(None, first=True)
    dice = yatzy_round(dice)
    dice = yatzy_round(dice)


if __name__ == "__main__":
    main()
