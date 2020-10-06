items = input().split('|')
budget = float(input())

new = []
sum_old_price = 0
sum_new_price = 0

for i in items:
    single_item = i.split('->')
    type = single_item[0]
    price = float(single_item[1])

    if budget < price:
        continue

    if type == 'Clothes':
        if price <= 50.00:
            budget -= price
            sum_old_price += price
            sum_new_price += price * 1.40
            new.append(price * 1.40)

    elif type == 'Shoes':
        if price <= 35.00:
            budget -= price
            sum_old_price += price
            sum_new_price += price * 1.40
            new.append(price * 1.40)

    elif type == 'Accessories':
        if price <= 20.50:
            budget -= price
            sum_old_price += price
            sum_new_price += price * 1.40
            new.append(price * 1.40)

for item in new:
    print(f'{item:.2f}', end= ' ')
print()

print(f'Profit: {sum_new_price - sum_old_price:.2f}')

if sum_new_price + budget >= 150:
    print(f'Hello, France!')
else:
    print('Time to go.')