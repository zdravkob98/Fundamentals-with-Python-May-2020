text = input()

explosion = 0

index = 0

while index != len(text):

    k = text[index]

    if text[index] == '>':
        explosion += int(text[index + 1])
        index += 1
        continue

    if explosion != 0:
        text = text[:index] + text[index:]
        explosion -= 1
        index -= 1

    index += 1

print(text)
