targets = list(map(int, input().split(' ')))
command = input()
indexes = []
while command != 'End':
    index = int(command)

    if index > len(targets) -1:
        command = input()
        continue

    if index in indexes:
        continue
    elif index not in indexes:
        indexes.append(index)

        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            if i == index:
                continue
            if targets[i] > targets[index]:
                targets[i] -= targets[index]
            elif targets[i] <= targets[index]:
                targets[i] += targets[index]

        targets[index] = -1

    command = input()

str_targets = list(map(str,targets))
length = targets.count(-1)
print(f"Shot targets: {length} -> {' '.join(str_targets)} ")