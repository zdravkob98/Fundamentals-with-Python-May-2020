numbers = list(map(int, input().split('@')))
current_position = 0
succeed = 0

while True:
    command = input()
    if command == 'Love!':
        break
    help = command.split(' ')
    length = int(help[1])

    current_position += length
    if current_position >= len(numbers):
        current_position = 0

    numbers[current_position] -= 2
    if numbers[current_position] == 0:
        print(f"Place {current_position} has Valentine's day." )
        succeed += 1
    elif numbers[current_position] < 0:
        print(f"Place {current_position} already had Valentine's day." )

print(f"Cupid's last position was {current_position}." )
counter = len(numbers) - succeed
if counter == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {counter} places.' )
