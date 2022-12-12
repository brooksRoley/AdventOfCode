import re
file = open('./day5input.txt', "r")
lines = file.read().splitlines()

# Modify the inputs into an array of arrays of strings.
# Hack to manipulate the input via text manipulation outside of python.
matrix = [
    ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q'],
    ['W', 'D', 'B', 'G'],
    ['F', 'W', 'R', 'T', 'S', 'Q', 'B'],
    ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N'],
    ['M', 'P', 'D', 'V', 'F'],
    ['F', 'W', 'J'],
    ['L', 'N', 'Q', 'B', 'J', 'V'],
    ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N'],
    ['J', 'S', 'Q', 'C', 'W', 'D', 'M']
]

for l in lines:
    digits = re.findall(r'\d+', l)
    [move, from_x, to_y] = [int(x) for x in digits]

    for i in range(move):
        x = matrix[from_x-1].pop()
        matrix[to_y-1].append(x)

result = []
for x in matrix:
    result.append(x[-1])
print(''.join(result))