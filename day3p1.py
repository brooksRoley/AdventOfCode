def score_round(x, y):
    priority = ''.join(set(x).intersection(y))
    output = score_letter(priority)
    return output

def score_letter(x):
    # a through z have priorities 1 through 26
    # A through Z have priorities 27 through 52
    if x.isupper():
        return ord(x) - 38
    else:
        return ord(x) - 96

strategy_guide = open('day3input.txt', 'r')
score = 0

for r in strategy_guide.read().splitlines():
    x, y = r[:len(r)//2], r[len(r)//2:]
    score += score_round(x, y)
    
print(score)