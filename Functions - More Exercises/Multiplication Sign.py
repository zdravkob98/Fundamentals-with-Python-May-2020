a = int(input())
b = int(input())
c = int(input())


def result(a, b, c):
    final_result = a * b * c
    if final_result < 0:
        return 'negative'
    elif final_result == 0:
        return 'zero'
    else:
        return 'positive'

print(result(a, b, c))