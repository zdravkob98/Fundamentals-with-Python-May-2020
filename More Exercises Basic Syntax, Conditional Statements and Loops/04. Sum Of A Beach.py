text = input()

word_one = 'water'
word_two = 'sand'
word_three = 'sun'
word_four = 'fish'
counter = 0

l = text.split()
for i in range(len(l)):
    l[i] = l[i].lower()



    for t in l:
        if word_one in t:
            counter += 1
    for t in l:
        if word_two in t:
            counter += 1
    for t in l:
        if word_three in t:
            counter += 1
    for t in l:
        if word_four in t:
            counter += 1

print(counter)

