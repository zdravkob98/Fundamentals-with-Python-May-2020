text = input()

for i in range(len(text)):
    if text[i] == ':':
        if text[i + 1] != ' ' and len(text[i + 1]) <= len(text):
            print(f'{text[i]}{text[i +1]}')
