data = input()
heroes = {}


while data != 'End':
    tolken = data.split(' ')
    command = tolken[0]
    hero_name = tolken[1]

    if command == 'Enroll':
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []


    elif command == 'Learn':
        spell = tolken[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell}.")
        else:
            heroes[hero_name].append(spell)


    elif command == 'Unlearn':
        spell_name = tolken[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

    data = input()

heroes = sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0]))
print('Heroes:')
for k,v in heroes:
    if len(v) > 0:
        v = ', '.join(v)
    else:
        v = ''
    print(f'== {k}: {v}')



