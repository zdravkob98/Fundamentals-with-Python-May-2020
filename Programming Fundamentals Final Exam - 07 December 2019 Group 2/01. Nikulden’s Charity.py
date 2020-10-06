text = input()

data = input()
while data != 'Finish':
    tolken = data.split()
    command = tolken[0]

    if command == 'Replace':
        current_char = tolken[1]
        new_char = tolken[2]
        if current_char in text:
            text = text.replace(current_char, new_char)
            print(text)
            #maybe need to print else
    elif command == 'Cut':
        start_index = int(tolken[1])
        end_index = int(tolken[2])
        if 0 <= start_index <= len(text) - 1 and 0 <= end_index <= len(text) - 1:
            text = text[:start_index] + text[end_index + 1:]
            print(text)
        else:
            print('Invalid indexes!')
        #maybe need to be including end index YES!!!
    elif command == 'Make':
        type = tolken[1]
        if type == 'Upper':
            text = text.upper()
        if type == 'Lower':
            text = text.lower()
        print(text)
    elif command == 'Check':
        string = tolken[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command == 'Sum':
        start = int(tolken[1])
        end = int(tolken[2])
        if 0 <= start <= len(text) - 1 and 0 <= end <= len(text) - 1:
            substring = text[start:end + 1]
            sum = 0
            for char in substring:
                sum += ord(char)
            print(sum)
        else:
            print("Invalid indexes!")

    data = input()
