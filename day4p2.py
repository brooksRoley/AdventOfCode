file = open('./day4input.txt', "r")
lines = file.read().splitlines()

i = 0
for l in lines:
    [e1, e2] = l.split(",")
    [x1, y1] = e1.split('-')
    [x2, y2] = e2.split('-')
    set1 = set(range(int(x1), int(y1)+1))
    set2 = set(range(int(x2), int(y2)+1))
    if set1.intersection(set2):
        i+=1
print(i)