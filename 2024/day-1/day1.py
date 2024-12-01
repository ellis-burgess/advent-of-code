list1 = []
list2 = []

with open('input.txt') as f:
  for line in f:
    n1, n2 = line.split()
    list1.append(int(n1))
    list2.append(int(n2))

total = 0
similarity = 0
found_nums = {}

for loc1, loc2 in zip(sorted(list1), sorted(list2)):
  total += abs(loc1 - loc2)
  if loc1 not in found_nums:
    found_nums[loc1] = len([i for i in list2 if i == loc1])
  similarity += (found_nums[loc1] * loc1)

print(total)
print(similarity)