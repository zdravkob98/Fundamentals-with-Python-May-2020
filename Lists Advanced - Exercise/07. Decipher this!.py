text = input().split()


def parse_char (word):
    temp = ''
    for ch in word:
        if str(ch).isdigit():
            temp += ch

    char_number = int(temp)
    char = chr(int(temp))
    new_word = word.replace(temp , char)
    return new_word


def replace(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return ''.join(temp)


def result (word):
    res = parse_char(word)
    res = replace(res)
    return res


new_word = [result(word) for word in text]
print(' '.join(new_word))