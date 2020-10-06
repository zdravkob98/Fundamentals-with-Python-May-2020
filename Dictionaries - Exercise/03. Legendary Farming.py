key_materials = {'fragments': 0, 'motes': 0, 'shards': 0 }
junk = {}
found = False


while not found:
    inventory_list = input().split()

    for i in range(0, len(inventory_list), 2):
        number = int(inventory_list[i])
        material = inventory_list[i + 1].lower()

        if material in key_materials and not found:
            key_materials[material] += number

            for material, number in key_materials.items():
                if material == 'shards' and number >= 250 and not found:
                    key_materials['shards'] = number - 250
                    print('Shadowmourne obtained!')
                    found = True
                elif material == 'fragments' and number >= 250 and not found:
                    key_materials['fragments'] = number - 250
                    print('Valanyr obtained!')
                    found = True
                elif material == 'motes' and number >= 250 and not found:
                    key_materials['motes'] = number - 250
                    print('Dragonwrath obtained!')
                    found = True

        elif material in junk and not found:
            junk[material] += number
        elif not found:
            junk[material] = number


key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
for item, value in key_materials.items():
    print(f'{item}: {value}')

junk = dict(sorted(junk.items(), key=lambda x: x[0]))
for item, value in junk.items():
    print(f'{item}: {value}')