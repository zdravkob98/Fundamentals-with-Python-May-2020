gift = input().split()

text = input()

while text != 'No Money':
    second_input = text.split()
    command = second_input[0]
    current_gift = second_input[1]


    if command == 'OutOfStock':
        for i in range(len(gift)):
            if gift[i] == current_gift:
                gift[i] = 'None'


    elif command == 'Required':
        index = int(second_input[2])
        if len(gift) > index and index >= 0:
            gift[index] = current_gift

    elif command == 'JustInCase':
        gift[-1] = current_gift

    text = input()
result = []
for e in gift:
    if e != 'None':
        result.append(e)
final_result = ' '.join(result)
print(final_result)