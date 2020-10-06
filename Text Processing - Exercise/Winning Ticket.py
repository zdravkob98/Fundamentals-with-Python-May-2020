text = input().split(', ')


for word in text:
    word = word.strip()

    a = 0
    b = 0
    c = 0
    d = 0

    aa = 0
    bb = 0
    cc = 0
    dd = 0

    if len(word) == 20:

        for i in range(10):
            if word[i] == '@':

                if a + 1 >= 6:
                    a += 1
                elif i == (len(word) / 2) - 1:
                    a += 1
                elif word[i + 1] == '@':
                    a += 1
                else:
                    a = 0
            if word[i] == '#':
                if b + 1 >= 6:
                    b += 1
                elif i == (len(word) / 2) - 1:
                    b += 1
                elif word[i + 1] == '#':
                    b += 1
                else:
                    b = 0

            if word[i] == '$':
                if c + 1 >= 6:
                    c += 1
                elif i == (len(word) / 2) - 1:
                    c += 1
                elif word[i + 1] == '$':
                    c += 1
                else:
                    c = 0

            if word[i] == '^':
                if d + 1 >= 6:
                    d += 1
                elif i == (len(word) / 2) - 1:
                    d += 1
                elif word[i + 1] == '^':
                    d += 1
                else:
                    d = 0

        for index in range(10,20):
            if word[index] == '@':
                if aa + 1>= 6:
                    aa += 1
                elif index == len(word) - 1:
                    aa += 1
                elif word[index + 1] == '@':
                    aa += 1
                else:
                    aa = 0

            if word[index] == '#':
                if bb + 1 >= 6:
                    bb += 1
                elif index == len(word)- 1:
                    bb += 1
                elif word[index + 1] == '#':
                    bb += 1
                else:
                    bb = 0

            if word[index] == '$':
                if cc + 1 >= 6:
                    cc += 1
                elif index == len(word)- 1:
                    cc += 1
                elif word[index + 1] == '$':
                    cc += 1
                else:
                    cc = 0

            if word[index] == '^':
                if dd + 1 >= 6:
                    dd += 1
                elif index == len(word)- 1:
                    dd += 1
                elif word[index + 1] == '^':
                    dd += 1
                else:
                    dd = 0




        if 9 >= a >= 6 and 9 >= aa >= 6 :
            match = min(a,aa)
            symbol = '@'
            print(f'ticket "{word}" - {match}{symbol}')
        elif 9 >= b >= 6 and 9 >= bb >= 6:
            match = min(b , bb)
            symbol = '#'
            print(f'ticket "{word}" - {match}{symbol}')
        elif 9 >= c >= 6 and 9 >= cc >= 6:
            match = min(c, cc)
            symbol = '$'
            print(f'ticket "{word}" - {match}{symbol}')
        elif 9 >= d >= 6 and 9 >= dd >= 6:
            match = min(d, dd)
            symbol = '^'
            print(f'ticket "{word}" - {match}{symbol}')

        elif a == 10 and aa == 10 :
            symbol = '@'
            print(f'ticket "{word}" - {10}{symbol} Jackpot!')
        elif b == 10 and bb == 10 :
            symbol = '#'
            print(f'ticket "{word}" - {10}{symbol} Jackpot!')
        elif c == 10 and cc == 10 :
            symbol = '$'
            print(f'ticket "{word}" - {10}{symbol} Jackpot!')
        elif d == 10 and dd == 10 :
            symbol = '^'
            print(f'ticket "{word}" - {10}{symbol} Jackpot!')
        elif a == 0 or aa == 0 :
            print(f'ticket "{word}" - no match')
        elif b == 0 or bb == 0 :
            print(f'ticket "{word}" - no match')
        elif c == 0 or cc == 0 :
            print(f'ticket "{word}" - no match')
        elif d == 0 or dd == 0 :
            print(f'ticket "{word}" - no match')


    else:
        print('invalid ticket')