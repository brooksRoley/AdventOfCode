# Find all of the directories with a total size of at most 100000,
# then calculate the sum of their total sizes.
# In the example above,
# these directories are a and e;
# the sum of their total sizes is 95437 (94853 + 584)

def process(command):
    # if isdigit(x[0]):
    sum = 0
    # for d in directories:
    #     if size[d] <= 100000:
    #         sum += size[d]
    return sum

file = open('./day7input.txt', "r")
lines = file.read().splitlines()

directories = {
    '/': []
}
contents = []
current_directory = ['/']

for l in lines:
    x = l.split(" ")
    if x[0] == "$":
        if x[1] == "cd":
            if x[2] == "..":
                current_directory.pop()
            else:
                current_directory.append(x[2])
        if x[1] == "ls":
            cd = "".join(current_directory)
            directories[cd] = directories[cd] + contents
            contents = []

    else:
        contents.append(l)



# Keep track of what directory you start from
# and when they change directory.
    # can add onto the directory tree
    # can pop off the directory.

# Can recognize a file as something that starts with a number.
# Can recognize a directory when it starts with a 'dir'.


# Write a function to traverse the directory structure
# sum sizes.
