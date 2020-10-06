n = int(input())

for i in range(n):
    text = input()
    name = ''
    age = ''
    name_flag = False
    age_flag = False

    for i in range(len(text)):
        char = text[i]
        if name_flag:
            name += text[i]
        if age_flag:
            age += text[i]
        if i  < len(text) - 1:
            if text[i + 1] == '|':
                name_flag = False
            elif text[i + 1] == '*':
                age_flag = False

        if text[i] == '@':
            name_flag = True
        elif text[i] == '#':
            age_flag = True

    print(f'{name} is {age} years old.')