targets = [int(x) for x in input().split(' ')]

while True:
    tokens = input().split(' ')
    attack = tokens[0]
    index = 0
    n = 0

    if attack == "Shoot":
        index = int(tokens[1])
        n = int(tokens[2])

        if 0 <= index < len(targets):
            targets[index] -= n

            if targets[index] <= 0:
                targets.pop(index)

    elif attack == "Add":
        index = int(tokens[1])
        n = int(tokens[2])

        if 0 <= index < len(targets):
            targets.insert(index, n)
        else:
            print("Invalid placement!")

    elif attack == "Strike":
        index = int(tokens[1])
        radius = int(tokens[2])

        start = index - radius
        end = index + radius

        if start >= 0 and end < len(targets):
            del targets[start: end + 1]
        else:
            print("Strike missed!")

    elif attack == "End":
        targets = [str(x) for x in targets]
        print("|".join(targets))
        break