def score_round(x, y):
    score = 0
    picks = { 'X': 1, 'Y': 2, 'Z': 3}
    subs = { 'X': 'A', 'Y': 'B', 'Z': 'C'}
    wins = { 'X': 'C', 'Y': 'A', 'Z': 'B'}
    if x == subs[y]:
        score += 3
    elif x == wins[y]:
        score += 6
    score += picks[y]    

    return score


strategy_guide = open('day2input.txt', 'r')
score = 0

for r in strategy_guide.read().splitlines():
    [x, y] = r.split(" ")
    score += score_round(x, y)

print(score)