text = input()

index = 0
string = ''
n = []
new_text = ''

while index < len(text):

    if text[index].isdigit():
        n.append(text[index])

        if index + 1 == len(text):
            num =int( ''.join(n))
            new_text += string.upper() * num
            n = []
            
            string = ''

        elif text[index +1].isdigit():
            index += 1
            continue
        else :
            num =int(''.join(n))
            new_text += string.upper() * num
            n = []
            string = ''

    else:
        string += text[index]

    index += 1

count = list(set(new_text))

print(f'Unique symbols used: {len(count)}')
print(new_text)