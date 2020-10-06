text = input()
list = []

for num in text:
    if int(num) >= 0 :
        num = int(-num)
        list.append(num)
    else:
        num = + num
        list.append(num)

print(list)