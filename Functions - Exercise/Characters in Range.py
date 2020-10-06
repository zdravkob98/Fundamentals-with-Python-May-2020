a = input()
b = input()


def returns_str(a , b):
    res = ''

    first_number = ord(a)
    second_number = ord(b)

    for i in range(first_number + 1, second_number ):
        char = chr(i)
        res += char
        res += ' '

    return res


print(returns_str(a , b))





