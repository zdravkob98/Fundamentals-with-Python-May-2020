record = {}
unlike = 0

while True:
    data = input().split('-')
    command = data[0]
    if command == 'Stop':
        break
    guest = data[1]
    meal = data[2]


    if command == 'Like':
        if guest not in record:
            record[guest] = []
        if meal not in record[guest]:
            record[guest].append(meal)


    elif command == 'Unlike':
        if guest not in record:
            print(f"{guest} is not at the party.")
        elif meal not in record[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            record[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")

            unlike += 1


record = sorted(record.items(), key=lambda x: (-len(x[1]), x[0]))

for k,v in record:
    meals = []
    for i in v:
        meals.append(i)
    print(f"{k}: {', '.join(meals)}")

print(f'Unliked meals: {unlike}')
