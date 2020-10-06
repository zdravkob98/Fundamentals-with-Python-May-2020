n = int(input())

plants = {}
for _ in range(n):
    data = input()
    if '<->' not in data:
        print('error')
    else:
        tolken = data.split('<->')
        plant = tolken[0]
        rarity = float(tolken[1])
        if plant not in plants:
            plants[plant] = [0, 0, 0]
            plants[plant][0] = rarity

        else:
            plants[plant][0] = rarity

data = input()
while data != 'Exhibition':
    tolk = data.split(': ')
    command = tolk[0]

    if command == 'Rate':
        tolken2 = tolk[1].split(' - ')
        plant = tolken2[0]
        if plant in plants:
            rating = float(tolken2[1])
            plants[plant][1] += rating
            plants[plant][2] += 1
        else:
            print('error')

    elif command == 'Update':
        tolken3 = tolk[1].split(' - ')
        plant = tolken3[0]
        if plant in plants:
            rarity2 = float(tolken3[1])
            plants[plant][0] = rarity2
        else:
            print('error')

    elif command == 'Reset':
        tolken4 = tolk[1].split(' - ')
        plant = tolken4[0]
        if plant in plants:
            plants[plant][1] = 0
            plants[plant][2] = 0
        else:
            print('error')
    else:
        print('error')
    data = input()

plants = sorted(plants.items(), key=lambda x: ( -x[1][0], -x[1][1]))
print('Plants for the exhibition:')
for k,v in plants:
    if v[2] == 0:
        print(f'- {k}; Rarity: {int(v[0])}; Rating: {v[1]:.2f}')
    else:
        print(f'- {k}; Rarity: {int(v[0])}; Rating: {v[1] / v[2]:.2f}')