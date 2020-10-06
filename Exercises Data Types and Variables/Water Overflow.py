n = int(input())
CAPACITY = 255
total_water = 0

for i in range(n):
    quantities_of_water = int(input())
    if CAPACITY < quantities_of_water:
        print(f'Insufficient capacity!')
    else:
        CAPACITY -= quantities_of_water
        total_water += quantities_of_water
print(f'{total_water}')
