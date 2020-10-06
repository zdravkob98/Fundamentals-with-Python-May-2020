from _collections import defaultdict

text = input()

my_dict = defaultdict(int)

for char in text:
    if char == ' ':
        continue
    else:
        #if char not in my_dict:
           # my_dict[char] = 0
        my_dict[char] += 1

for key, value in my_dict.items():
    print(f'{key} -> {value}')