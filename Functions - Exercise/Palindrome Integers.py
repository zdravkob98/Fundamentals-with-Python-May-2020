numbers = input().split(', ')


def palindrome(numbers):
    for num in numbers:
        length = len(num)
        new_n= ''
        for i in range(length - 1, -1, -1):
            res = num[i]
            new_n += res
        if num == new_n:
            print(True)
        else:
            print(False)

palindrome(numbers)