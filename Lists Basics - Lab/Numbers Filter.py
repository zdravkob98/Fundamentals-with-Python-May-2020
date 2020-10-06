n = int(input())
l = []
l2 = []
for i in range(n):
    num = int(input())
    l2.append(num)

command = input()

for e in l2:
    if command == 'even':
        if e % 2 == 0:
            l.append(e)
    elif command == 'odd':
        if e % 3 == 0:
            l.append(e)
    elif command == 'positive':
        if e >= 0:
            l.append(e)
    elif command == 'negative':
        if e < 0:
            l.append(e)

print(l)