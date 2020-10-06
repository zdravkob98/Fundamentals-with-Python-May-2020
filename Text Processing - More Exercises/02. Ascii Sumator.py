a = input()
b = input()
text = input()

char = ord(a)
char = ord(b)

sum = 0

for char in text:
    num = ord(char)
    if char < num < char:
        sum += num
print(sum)