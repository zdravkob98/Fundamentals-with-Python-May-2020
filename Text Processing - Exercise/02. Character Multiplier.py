text = input().split()
first = text[0]
second = text[1]


total_sum = 0

index = min(len(first), len(second))

for i in range(index):
    total_sum += ord(first[i]) * ord(second[i])

if len(first) > len(second):
    for a in range(index, len(first)):
        total_sum += ord(first[a])
else:
    for a in range(index, len(second)):
        total_sum += ord(second[a])

print(total_sum)