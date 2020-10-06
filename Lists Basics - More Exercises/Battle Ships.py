n = int(input())
all = []
count = 0

for i in range(n):
    line = list(map(int, input().split()))
    all.append(line)






attack = input().split()
for target in attack:
    target = target.split('-')
    row = int(target[0])
    cow = int((target[1]))
    if all[row][cow] != 0:
        all[row][cow] -= 1
    else:
        continue
    if all[row][cow] == 0 :
        count += 1
print(count)