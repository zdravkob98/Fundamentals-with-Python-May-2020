string = input()


def print_digits(string):
    digit = ''
    for char in string:
        if char.isdigit():
            digit += char
    return digit


def print_letter(string):
    letter = ''
    for char in string:
        if char.isalpha():
            letter += char
    return letter


def print_other(string):
    other = ''
    for char in string:
        if not char.isdigit() and not char.isalpha():
            other += char
    return other

print(print_digits(string))
print(print_letter(string))
print(print_other(string))


