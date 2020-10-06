def smallest_of_three_numbers(a , b , c):
    res = 0

    if a < b and a < c :
        res = a
    elif b < c and b < a :
        res = b
    else:
        res = c

    return res


a = int(input())
b = int(input())
c = int(input())

print(smallest_of_three_numbers(a,b,c))