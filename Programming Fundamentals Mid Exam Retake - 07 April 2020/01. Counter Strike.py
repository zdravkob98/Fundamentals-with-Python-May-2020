initial_energy = int(input())
command = input()

count = 0
flag = False

while command != 'End of battle':
    distance = int(command)

    if distance > initial_energy:
        print(f"Not enough energy! Game ends with {count} won battles and {initial_energy} energy")
        flag = True
        break
    else:
        initial_energy -= distance
        count += 1
    command = input()
    if count % 3 == 0:
        initial_energy += count

if not flag :
    print(f"Won battles: {count}. Energy left: {initial_energy}")