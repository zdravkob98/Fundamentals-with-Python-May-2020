username = input()

data = input()
while data != 'Sign up':
    tolken = data.split()
    command = tolken[0]

    if command == 'Case':
        type = tolken[1]
        if type == 'lower':
            username = username.lower()
        elif type == 'upper':
            username = username.upper()
        print(username)
    elif command == 'Reverse':
        start_index = int(tolken[1])
        end_index = int(tolken[2])
        if 0 <= start_index <= len(username) - 1 and 0 <= end_index <= len(username) - 1:
            substring = username[start_index:end_index + 1]
            print(substring[::-1])
    elif command == 'Cut':
        substring = tolken[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == 'Replace':
        char = tolken[1]
        username = username.replace(char, '*')
        print(username)
    elif command == 'Check':
        char = tolken[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")


    data = input()