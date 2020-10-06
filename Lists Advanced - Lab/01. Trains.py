n_wagons = int(input())
wagons = [0] * n_wagons

command = input()

while command != 'End':
    tokens = command.split()
    command = tokens[0]


    if command == 'add':
        people = int(tokens[1])
        wagons[-1] += people
    elif command == 'insert':
        index = int(tokens[1])
        people = int(tokens[2])
        wagons[index] += people
    elif command == 'leave':
        index = int(tokens[1])
        people = int(tokens[2])
        wagons[index] -= people
    command = input()

print(wagons)




