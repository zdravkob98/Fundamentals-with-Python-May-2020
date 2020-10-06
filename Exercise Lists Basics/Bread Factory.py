day_events = input().split('|')

coins = 100
energy = 100

flag = True

for e in day_events:
    event = e.split('-')
    command = event[0]
    num = int(event[1])

    if command == 'rest':
        if energy >= 100:
            print(f'You gained {0} energy.')
            print(f'Current energy: {energy}.')

        elif energy + num >= 100:
            print(f'You gained {100 - energy} energy.')
            energy = 100
            print(f'Current energy: {energy}.')
        else:
            print(f'You gained {num} energy.')
            energy += num
            print(f'Current energy: {energy}.')

    elif command == 'order':
        if energy >= 30:
            print(f'You earned {num} coins.')
            coins += num
            energy -= 30
        else:
            print('You had to rest!')
            energy += 50

    else:
        coins -= num
        if coins > 0:
            print(f'You bought {command}.')
        else:
            print(f'Closed! Cannot afford {command}.')
            flag = False
            break
if flag == True:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')