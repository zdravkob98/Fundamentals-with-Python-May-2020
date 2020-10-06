text = input()
new_str = ''
length = len(text)

for i in range(length):
    if i == length - 1:
        new_str += text[i]
    elif text[i] != text[i + 1]:
        new_str += text[i]

print(new_str)