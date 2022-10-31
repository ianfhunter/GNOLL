
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

    if(all(dice[0] == dice)):
        five_oak = 50
    
    # hello

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
