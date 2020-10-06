text = input()


data = input()

while data != 'Done':
    tolken = data.split(' ')
    command = tolken[0]

    if command == 'TakeOdd':
        new_str = ''
        for i in range(len(text)):
            if i % 2 == 1:
                new_str += text[i]
        text = new_str
        print(text)

    elif command == 'Cut':
        index = int(tolken[1])
        length = int(tolken[2])
        text = text[:index] + text[index + length:]

        print(text)

    elif command == 'Substitute':
        substring = tolken[1]
        substitute = tolken[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    data = input()

print(f'Your password is: {text}')
