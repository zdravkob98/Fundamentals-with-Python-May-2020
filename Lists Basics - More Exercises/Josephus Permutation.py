text = list(map(int, input().split()))
k = int(input())
l = []

step = 1
index = 0
while len(text):
    if len(text) <= index:
        index = 0
    if step % k == 0:
        n = text.pop(index)
        l.append(n)
        index -= 1
    step += 1
    index += 1
print(l)
