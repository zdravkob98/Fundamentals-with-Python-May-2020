def is_int(text):
    return int(text) * 2

def is_real(text):
    result = (float(text) * 1.5)
    return result

def is_string(text):
    return f'${text}$'




command = input()
text = input()


if command == 'int':
    print(is_int(text))
elif command == 'real':
    print(f'{is_real(text):.2f}')
else:
    print(is_string(text))