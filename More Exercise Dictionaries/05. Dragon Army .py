n = int(input())

dragons = {}

for i in range(n):
    dragon = input().split()
    type = dragon[0]
    name = dragon[1]
    damage = dragon[2]
    health = dragon[3]
    armor = dragon[4]

    if health == 'null':
        health = 250
    if damage == 'null':
        damage = 45
    if armor == 'null':
        armor = 10

    value = [health, damage, armor]
    if type not in dragons:
        dragons[type] = {name: value}
    elif name not in dragons[type]:
        dragons[type][name] = value
    else:
        dragons[type][name] = value

for k, v in dragons.items():
    da = 0
    he = 0
    ar = 0
    n = 0
    for k2, v2 in v.items():
        n += 1
        da += int(v2[0])
        he += int(v2[1])
        ar += int(v2[2])

    print(f'{k}::({he / n:.2f}/{da / n:.2f}/{ar / n:.2f})')
    v = dict(sorted(v.items(), key= lambda x:x[0]))
    for k1, v1 in v.items():
        d = v1[0]
        h = v1[1]
        a = v1[2]
        print(f'-{k1} -> damage: {h}, health: {d}, armor: {a}')