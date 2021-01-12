import random

result = {}

members = input().split()
lst = input().split()

random.shuffle(members)
random.shuffle(lst)

for i in range(len(members)):
    result[members[i]] = lst[i]

print(result)