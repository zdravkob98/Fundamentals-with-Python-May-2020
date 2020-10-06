string = list(map(int, input().split('@')))
text = input()
real_index = 0
succeed = 0
while text != 'Love!':
    command = text.split(' ')
    number = int(command[1])

    real_index += number
    if real_index >= len(string):
        real_index = 0

    string[real_index] -= 2
    if string[real_index] == 0:
        print(f"Place {real_index} has Valentine's day.")
        succeed += 1
    elif string[real_index] < 0:
        print(f"Place {real_index} already had Valentine's day.")

    text = input()

print(f"Cupid's last position was {real_index}.")
counter = len(string) - succeed
if counter == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {counter} places.' )