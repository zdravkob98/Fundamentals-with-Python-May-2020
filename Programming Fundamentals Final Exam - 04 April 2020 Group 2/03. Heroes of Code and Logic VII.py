n = int(input())

heroes = {}

for i in range(n):
    tolken = input().split(' ')
    hero = tolken[0]
    hp = int(tolken[1])
    mp = int(tolken[2])

    if hero not in heroes:
        heroes[hero] = [hp, mp]

data = input()

while data != 'End':
    tolken = data.split(' - ')
    command = tolken[0]
    hero = tolken[1]

    if command == 'CastSpell':
        mp_needed = int(tolken[2])
        spell_name = tolken[3]
        if heroes[hero][1] >= mp_needed:
            heroes[hero][1] -= mp_needed
            print(f'{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!')
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")


    elif command == 'TakeDamage':
        damage = int(tolken[2])
        attacker = tolken[3]
        heroes[hero][0] -= damage
        if heroes[hero][0] > 0:
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!')
        else:
            heroes.pop(hero)
            print(f'{hero} has been killed by {attacker}!')


    elif command == 'Recharge':
        amount = int(tolken[2])

        if heroes[hero][1] + amount > 200:
            amount_recovered = 200 - heroes[hero][1]
            heroes[hero][1] = 200
            print(f'{hero} recharged for {amount_recovered} MP!')
        elif heroes[hero][1] + amount <= 200:
            heroes[hero][1] += amount
            print(f'{hero} recharged for {amount} MP!')


    elif command == 'Heal':
        amount = int(tolken[2])

        if heroes[hero][0] + amount > 100:
            amount_heal = 100 - heroes[hero][0]
            heroes[hero][0] = 100
            print(f"{hero} healed for {amount_heal} HP!")
        elif heroes[hero][0] + amount <= 100:
            heroes[hero][0] += amount
            print(f"{hero} healed for {amount} HP!")

    data = input()

heroes = sorted(heroes.items(), key= lambda x: (-x[1][0], x[0]))

for k,v in heroes:
    print(f'{k}')
    print(f'HP: {v[0]}')
    print(f'MP: {v[1]}')