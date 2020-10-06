text = input()
new_str = ''

for char in text:
    n = ord(char) + 3
    c = chr(n)
    new_str += c
print(new_str)