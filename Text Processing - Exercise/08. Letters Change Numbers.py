text = input().split()
total_sum = 0


for word in text:

    index = 0
    first = False
    ch_1 = ''
    ch_2 = ''
    n = []

    while index != len(word):

        if word[index].isalpha() and first == False:
            ch_1 += word[index]
            first = True

        elif word[index].isalpha() and first == False:
            ch_1 += word[index]
            first = True

        elif word[index].isalpha() and first == True:
            ch_2 += word[index]

        elif word[index].isalpha() and first == True:
            ch_2 += word[index]


        if word[index].isdigit():
            n.append(word[index])

        index += 1

    num = int(''.join(n))
    if ch_1.isupper():
        total_sum += num / (ord(ch_1) - 64)
    elif ch_1.islower():
        total_sum += (ord(ch_1) - 96) * num

    if ch_2.isupper():
        total_sum -= ord(ch_2) - 64
    elif ch_2.islower():
        total_sum += ord(ch_2) - 96

print(f'{total_sum:.2f}')