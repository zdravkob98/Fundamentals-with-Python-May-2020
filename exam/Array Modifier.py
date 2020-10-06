numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == 'end':
        break
    else:
        tolken = command.split()
        comm = tolken[0]

        if comm == 'swap':
            index1 = int(tolken[1])
            index2 = int(tolken[2])
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

        elif comm == 'multiply':
            index1 = int(tolken[1])
            index2 = int(tolken[2])
            numbers[index1] = numbers[index1] * numbers[index2]

        elif comm == 'decrease':
            numbers = [n - 1 for n in numbers]


numbers = list(map(str,numbers))
print(', '.join(numbers))