n = int(input())
word = input()

l1 = []
l2 = []
for i in range(n):
    text = input()
    l1.append(text)
for t in l1:
    if word in t:
        l2.append(t)

print(l1)
print(l2)