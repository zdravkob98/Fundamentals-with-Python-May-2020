stop_destination = input()

data = input()
while data != 'Travel':
    tolken = data.split(':')
    command = tolken[0]

    if command == 'Add Stop':
        index = int(tolken[1])
        string = tolken[2]
        if 0 <= index < len(stop_destination):
            stop_destination = stop_destination[:index] + string + stop_destination[index:]
        print(stop_destination)

    elif command == 'Remove Stop':
        start_index = int(tolken[1])
        end_index = int(tolken[2])
        if 0 <= start_index < len(stop_destination) and 0 <= end_index < len(stop_destination):
            stop_destination = stop_destination[:start_index] + stop_destination[end_index + 1:]
        print(stop_destination)


    elif command == 'Switch':
        old_string = tolken[1]
        new_string = tolken[2]
        if old_string in stop_destination:
            stop_destination = stop_destination.replace(old_string, new_string)
        print(stop_destination)
    data = input()

print(f"Ready for world tour! Planned stops: {stop_destination}")