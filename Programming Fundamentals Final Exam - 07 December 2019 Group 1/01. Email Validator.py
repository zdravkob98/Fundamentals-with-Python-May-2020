email = input()

data = input()
while data != 'Complete':

    if data == 'Make Upper':
        email = email.upper()
        print(email)
    elif data == 'Make Lower':
        email = email.lower()
        print(email)
    elif data == 'GetUsername':
        if '@' in email:
            substring = ''
            for c in email:
                if c == '@':
                    break
                else:
                    substring += c
            print(substring)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif data == 'Encrypt':
        ascii_value = []
        for ch in email:
            ascii_value.append(str(ord(ch)))
        print(f"{' '.join(ascii_value)}")

    tolken = data.split()
    command = tolken[0]

    if command == 'GetDomain':
        count = int(tolken[1])
        text_for_print = ''
        for n in range(1, count + 1):
            text_for_print += email[-n]
        print(text_for_print[::-1])
    elif command == 'Replace':
        char = tolken[1]
        email = email.replace(char, '-')
        print(email)

    data = input()