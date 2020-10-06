health = 100
bitcoin = 0

rooms = input().split('|')
for i in range( len(rooms)):
    tolken = rooms[i].split(' ')
    command = tolken[0]
    number = int(tolken[1])

    if command == 'potion':
        if health == 100 :
            print("You healed for 0 hp.")
        elif health + number > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
        else:
            health += number
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == 'chest':
        bitcoin += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}." )
            print(f"Best room: {i +1}")
            break

if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")
