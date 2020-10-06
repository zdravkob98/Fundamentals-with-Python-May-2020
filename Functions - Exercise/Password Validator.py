def len_password(passward):

    if 6 <= len(password) <= 10:
        return True
    else:
        return


def only_of_letters_and_digits(password):
    for char in password:
        if char.isalpha() or char.isdecimal():
            continue
        else:
            return
    return True


def two_digit(password):
    counter = 0
    for char in password:
        if char.isdecimal():
            counter += 1

    if counter >= 2 :
        return True
    else:
        return


password = input()

result1 = len_password(password)
result2 = only_of_letters_and_digits(password)
result3 = two_digit(password)

if result1 == True and result2 == True and result3 == True:
    print("Password is valid")
else:
    if result1 == None:
        print("Password must be between 6 and 10 characters")
    if result2 == None:
        print("Password must consist only of letters and digits")
    if result3 == None:
        print("Password must have at least 2 digits")


