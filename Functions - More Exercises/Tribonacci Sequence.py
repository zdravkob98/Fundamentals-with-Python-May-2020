n = int(input())

print(f'{1}', end=' ')


def result(n):
    a = 1
    b = 0
    c = 0

    number = a + b + c

    for i in range(n - 1):
        number = a + b + c
        print(f'{number}', end=' ')
        c = b
        b = a
        a = number


result(n)
