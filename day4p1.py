file = open('./day4input.txt', "r")
lines = file.read().splitlines()

def includes(x, y):
    print(x, y)

i = 0
for l in lines:
    [e1, e2] = l.split(",")
    [x, y] = e1.split('-')
    set1 = set(range(int(x), int(y)+1))
    [x, y] = e2.split('-')
    set2 = set(range(int(x), int(y)+1))
    print(set1, set2)
    if set1.issubset(set2) or set2.issubset(set1):
        i+=1
print(i)