dwarfs = {}
colors = {}

data = input()
while data != 'Once upon a time':
    data = data.split(" <:> ")

    dwarf_name = data[0]
    color = data[1]
    physics = int(data[2])
    if (color, dwarf_name) not in dwarfs:
        colors[color] = colors.get(color, 0) + 1
        dwarfs[color, dwarf_name] = [physics, color]
    else:
        if dwarfs[color, dwarf_name][0] < physics:
            dwarfs[color, dwarf_name] = [physics, color]

    data = input()

dwarf_name = dict(sorted(dwarfs.items(), key=lambda x: (-x[1][0], -colors[x[1][1]])))

for key, value in dwarf_name.items():
    name = key[1]
    [physic, color] = value
    print(f"({color}) {name} <-> {physic}")