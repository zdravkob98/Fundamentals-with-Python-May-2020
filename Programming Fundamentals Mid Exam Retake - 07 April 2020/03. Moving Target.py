targets = list(map(int, input().split(' ')))

command = input()

while command != 'End':
    command = command.split(' ')
    attack = command[0]
    index = int(command[1])
    n = int(command[2])

    if attack == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= n
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif attack == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, n)
        else:
            print("Invalid placement!")

    elif attack == 'Strike':
        radius_start = index - n
        radius_end = index + n

        if 0 <= radius_start < len(targets) and 0 <= radius_end < len(targets):

            del targets[radius_start: radius_end + 1]
        else:
            print("Strike missed!")
    command = input()

print('|'.join(list(map(str, targets))))

