from collections import Counter


def is_low_straight(dice):
    return False

def is_high_straight(dice):
    return True

def scorecard (dice):

    tot_sides = lamda y : sum([x for x in dice if x == y])

    top = [
       tot_sides(1),
       tot_sides(2),
       tot_sides(3),
       tot_sides(4),
       tot_sides(5),
       tot_sides(6),
    ]

    top_bonus = 50 if sum(top) >= 63 else 0

    one_pair_sum = 0
    two_pair_sum = 0
    three_oak_sum = 0
    four_oak_sum = 0
    low_straight = 0
    high_straight = 0
    full_house = 0
    chance = 0
    five_oak = 0

    foak = [a for a,b in Counter(dice).items() if b == 4])
    toak = [a for a,b in counter(dice).items() if b == 3])
    twoak = [a for a,b in Counter(dice).items() if b == 3])

    if(all(dice[0] == dice)):
        five_oak = 50
    elif(len(foak) >0):
        four_oak_sum = sum(foak)
    elif(len(toak) >0):
        if(len(twoak)>0):
            # full house
            full_house = sum(toak) + sum(twoak)
        else:
            three_oak_sum = sum(toak)
    elif(len(twoak) > 0):
        if len(twoak) == 2:
            two_pair_sum = sum(twoak)
        else:
            one_pair_sum = sum(twoak)
    elif is_low_straight(dice):
        low_straight = 15
    elif is_high_straight(dice):
        low_straight = 20
    else:
        chance= sum(dice)

    print(f"""
Dice: {dice}

[1]: {top[0]}
[2]: {top[1]}
[3]: {top[2]}
[4]: {top[3]}
[5]: {top[4]}
[6]: {top[5]}

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

Total: {}
    """)


def main():
    scorecard()

if __name__ == "__main__":
    main()
