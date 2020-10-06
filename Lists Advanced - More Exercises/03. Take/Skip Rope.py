text = input()
number = []

result = []

for char in text:
    if char.isdigit():
        number.append(int(char))
        text= text.replace(char, '', 1)




for i in range( len(number)):

    if i % 2 == 0 :

            for char in range(number[i]):
                if len(text) <= 0:
                    break
                result.append(text[0])
                text = text.replace(text[0], '', 1)
    else:

            for skip_num in range(number[i]):
                if len(text) <= 0:
                    break
                text = text.replace(text[0], '', 1)

print(''.join(result))