def score_round(x, y):
    score = 0
    picks = { 'X': 1, 'Y': 2, 'Z': 3}
    wins = { 'X': 0, 'Y': 3, 'Z': 6}

    copy = {
        # Rock
        'A': {
            'X': 'Z',
            'Y': 'X',
            'Z': 'Y',
        },
        # Paper
        'B': {
            'X': 'X',
            'Y': 'Y',
            'Z': 'Z',
        },
        # Scissors
        'C': {
            'X': 'Y',
            'Y': 'Z',
            'Z': 'X',
        }
    }
    return picks[copy[x][y]] + wins[y]


strategy_guide = open('day2input.txt', 'r')
score = 0

for r in strategy_guide.read().splitlines():
    [x, y] = r.split(" ")
    score += score_round(x, y)

print(score)