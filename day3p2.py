def score_round(x):
    l = set.intersection(set(x[0]), set(x[1]), set(x[2]))
    return score_letter(''.join(l))

def score_letter(x):
    # a through z have priorities 1 through 26
    # A through Z have priorities 27 through 52
    if x.isupper():
        return ord(x) - 38
    else:
        return ord(x) - 96

strategy_guide = open('day3input.txt', 'r')
score = 0
elves = []
for r in strategy_guide.read().splitlines():
    elves.append(r)
    if len(elves) == 3:
        score += score_round(elves)
        elves = []

print(score)
