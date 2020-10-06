text = input()

my_list = []


for c in text:
    if c.isupper():
        my_list += len(text[c])


print(my_list)