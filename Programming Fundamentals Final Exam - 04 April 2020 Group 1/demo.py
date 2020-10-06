data = input()

cities = {}

while data != 'Sail':
    tolken = data.split("||")
    city = tolken[0]
    population = int(tolken[1])
    gold = int(tolken[2])

    if city not in cities:
        cities[city] = {}
        if population not in cities[city]:
            cities[city] = [population , gold]

    else:
        cities[city][0] += population
        cities[city][1] += gold

    data = input()

command = input()
while command != 'End':
    tolken = command.split('=>')
    command = tolken[0]
    city = tolken[1]

    if command == 'Plunder':
        population = int(tolken[2])
        gold = int(tolken[3])
        cities[city][0] -= population
        cities[city][1] -= gold

        print(f'{city} plundered! {gold} gold stolen, {population} citizens killed.')

        if cities[city][0] <= 0 or cities[city][1] <= 0:
            print(f'{city} has been wiped off the map!')
            cities.pop(city)

    elif command == 'Prosper':
        gold = int(tolken[2])
        if gold >= 0:
            cities[city][1] += gold
            print(f'{gold} gold added to the city treasury. {city} now has {cities[city][1]} gold.')
        else:
            print("Gold added cannot be a negative number!")
    command = input()


print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
cities = sorted(cities.items(), key=lambda x: (-x[1][1], x[0]))
for k,v in cities:
    print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg')