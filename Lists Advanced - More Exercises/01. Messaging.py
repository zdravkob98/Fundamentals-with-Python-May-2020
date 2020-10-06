indexes = input().split()
text = input()
new_word = []

for index in indexes:
    i = 0
    for ch in index:
        i += int(ch)
    index_for_remove = i % len(text)

    for i in range(len(text)):
        if i == index_for_remove:
            new_word.append(text[index_for_remove])
            text = text.replace(text[index_for_remove], '', 1)
            break

print(''.join(new_word))

