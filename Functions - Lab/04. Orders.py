COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00


product = input()
quantity = int(input())


def calculate_total (quantity , product):
    total = None
    if product == 'coffee':
        total = quantity * COFFEE
    elif product == 'water':
        total = quantity * WATER
    elif product == 'coke':
        total = quantity * COKE
    elif product == 'snacks':
        total = quantity * SNACKS
    return f'{total:.2f}'


print(calculate_total(quantity , product))