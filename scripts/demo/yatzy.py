
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

    print(f"""
Dice: {dice}

[1]: {top[0]}
[2]: {top[1]}
[3]: {top[2]}
[4]: {top[3]}
[5]: {top[4]}
[6]: {top[5]}

Top Bonus: {top_bonus}
    """)


def main():
    scorecard()

if __name__ == "__main__":
    main()
