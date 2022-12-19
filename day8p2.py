import numpy as np

with open('./day8input.txt') as f:
    x = f.read().splitlines()
# Sample problem
# x = [
#     '30373',
#     '25512',
#     '65332',
#     '33549',
#     '35390',
# ]

def count(arr, height):
    s=0
    for x in arr:
        s+=1
        if x < height:
            continue
        else:
            return s
    return s

visible = np.array([ [int(height) for height in row.strip()] for row in x])
heights = np.array([[0 for value in row] for row in visible])

maxes = []
for i in range(len(visible)):
    for j in range(len(visible[0])):
        h = visible[i][j]
        left = count(np.flip(visible[i, :j]), h)
        right = count(visible[i, j+1:], h)
        top = count(np.flip(visible[:i,j]), h)
        down = count(visible[i+1:,j], h)
        height =  left * right * top * down
        heights[i, j] = height
        # print(h, height)
        # print(left, right, top, down)
        # print(np.flip(visible[i, :j]), visible[i, j+1:], np.flip(visible[:i,j]), visible[i+1:,j])
        # print("----------")
    maxes.append(max(heights[i]))

# print(heights)
print(max(maxes))