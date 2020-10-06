def read():
    first = []
    second = []
    for i in range(8):
        if len(first) < 4:
            first.append(float(input()))
        else:
            second.append(float(input()))

    return first, second


def longer_line():
    first, second = read()
    first_chk = [abs(x) for x in first]
    second_chk = [abs(x) for x in second]
    if sum(first_chk) > sum(second_chk):
        if first_chk[0] + first_chk[1] > first_chk[2] + first_chk[3]:
            return f'{int(first[2]), int(first[3])}{int(first[0]), int(first[1])}'
        else:
            return f'{int(first[0]), int(first[1])}{int(first[2]), int(first[3])}'
    else:
        if second_chk[0] + second_chk[1] > second_chk[2] + second_chk[3]:
            return f'{int(second[2]), int(second[3])}{int(second[0]), int(second[1])}'
        else:
            return f'{int(second[0]), int(second[1])}{int(second[2]), int(second[3])}'


print(longer_line())