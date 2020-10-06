key = int(input())
n = int(input())

for c in range(n):
    char = input()
    next_char = ord(char) + key
    result = chr(next_char)
    print(f'{result}', end='')