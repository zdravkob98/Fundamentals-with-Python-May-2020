text = list(map(int, input().split(', ')))
l = []
for n in text:
    if n == 0:
        text.remove(n)
        text.append(n)
print(text)