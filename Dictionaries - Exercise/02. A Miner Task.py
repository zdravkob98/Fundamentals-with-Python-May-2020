from _collections import defaultdict


my_dict = defaultdict(int)

while True:
    command = input()
    if command == 'stop':
        break
    money = int(input())

    my_dict[command] += money

for key, value in my_dict.items():
    print(f'{key} -> {value}')

