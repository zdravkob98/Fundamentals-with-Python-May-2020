targets = list(map(int, input().split(' ')))

command = input()

while command != 'End':
    command = command.split(' ')
    attack = command[0]
    index = int(command[1])
    n = int(command[2])

    if attack == 'Shoot':
        if 0 <= index <= len(targets) -1:
            targets[index] -= n
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif attack == 'Add':
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, n)
        else:
            print("Invalid placement!")

    elif attack == 'Strike':
        start = index - n
        end = index + n
        if 0 <= start <= len(targets) - 1 and 0 <= end <= len(targets):
            del targets[start:end + 1]

        else:
            print("Strike missed!")
    command = input()

print('|'.join(list(map(str, targets))))