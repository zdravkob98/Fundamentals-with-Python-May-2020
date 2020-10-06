from _collections import defaultdict

words = input().split()

my_dict = defaultdict(int)

for word in words:
    word = word.lower()
    my_dict[word] += 1

for word in my_dict:
    if my_dict[word] % 2 != 0:
        print(f'{word}', end= ' ')

