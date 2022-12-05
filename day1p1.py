def get_max_sum(list_nums):
  sums = []
  chunk = []
  for num in list_nums:
    if num == '':
      if chunk:
        sums.append(sum(chunk))
        chunk = []
    else:
      chunk.append(int(num))
  if chunk:
    sums.append(sum(chunk))
  return max(sums)

file = open('./day1input.txt', "r")
lines = file.read().splitlines()
print(get_max_sum(lines))