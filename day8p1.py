import numpy as np
x = open('./day8input.txt', "r")

# sample = [
#     '30373',
#     '25512',
#     '65332',
#     '33549',
#     '35390',
# ]

visible = np.array([ [int(height) for height in row.strip()] for row in x])
s = 0
for i in range(len(visible)):
    for j in range(len(visible[0])):
        current = visible[i, j]
        left = len(visible[i, :j]) == 0 or current > max(visible[i, :j])
        right = len((visible[i, j+1:])) == 0 or current > max(visible[i, j+1:])
        top = len((visible[:i, j])) == 0 or current > max(visible[:i,j])
        down = len((visible[i+1:, j])) == 0 or current > max(visible[i+1:,j])
        if left or right or top or down:
            s+=1

print(s)