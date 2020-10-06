sequence = input()

my_dict = {}

while sequence != 'buy':
    tolkens = sequence.split(' ')
    name = tolkens[0]
    price = float(tolkens[1])
    quantity = int(tolkens[2])

    if name not in my_dict:
        my_dict[name] = []
        my_dict[name].append(price)
        my_dict[name].append(quantity)

    else:
        my_dict[name][0] = price
        my_dict[name][1] += quantity

    sequence = input()

for key, value in my_dict.items():
    print(f'{key} -> {value[0] * value[1]:.2f}')