def sum_numbers(a , b):
    res = a + b
    return res


def subtract(a , b):
    res = a - b
    return res


def add_and_subtract(a , b ,c):
    result = sum_numbers(a , b)
    res = subtract(result,c)
    return res


a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a,b,c))