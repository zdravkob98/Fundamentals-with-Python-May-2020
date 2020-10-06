string = input().split('@')
string = list(map(int, string))
text = input()
succeed = 0
index = 0

while text != 'Love!':
    command = text.split(' ')
    jump = command[0]
    number = int(command[1])

    index += number
    if index > len(string) - 1:
        index = 0
        real_index = 0

    else:
        real_index = index
        #real_index = index % len(string)

    if string[real_index ] == 0:
        print(f"Place {real_index} already had Valentine's day.")

    elif string[real_index] - 2 == 0:
        print(f"Place {real_index} has Valentine's day.")
        string[real_index] -= 2
        succeed += 1

    else:
        string[real_index] -= 2

    text = input()

print(f"Cupid's last position was {real_index}.")
counter = len(string) - succeed
if counter == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {counter} places.' )