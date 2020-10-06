product = {}

command = input()

while True:
    if command == 'statistics':
        break

    new_product = command.split(': ')
    if new_product[0] not in product:
        product[new_product[0]] = 0
    product[new_product[0]] += int(new_product[1])

    command = input()

print("Products in stock:")
for p in product:
    print(f'- {p}: {product[p]} ')
product_count = len(product.keys())
print(f'Total Products: {product_count}')
print(f'Total Quantity: {sum(product.values())}')