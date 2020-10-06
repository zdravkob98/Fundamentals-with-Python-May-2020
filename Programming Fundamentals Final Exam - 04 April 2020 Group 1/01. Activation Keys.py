activation_key = input()

data = input()
while data != 'Generate':
    split_data = data.split('>>>')
    command = split_data[0]

    if command == 'Contains':
        substring = split_data[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')

    elif command == 'Flip':
        upper_lower = split_data[1]
        start_index = int(split_data[2])
        end_index = int(split_data[3])
        for i in range(start_index, end_index):
            if upper_lower == 'Upper':
                activation_key = activation_key[:start_index] + activation_key[
                                                                start_index:end_index].upper() + activation_key[
                                                                                                 end_index:]
            elif upper_lower == 'Lower':
                activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]

        print(activation_key)

    elif command == 'Slice':
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        for i in range(start_index, end_index):
            activation_key = activation_key.replace(activation_key[start_index], '', 1 )

        print(activation_key)

    data = input()

print(f'Your activation key is: {activation_key}')
