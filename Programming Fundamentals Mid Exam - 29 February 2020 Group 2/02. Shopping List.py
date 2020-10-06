groceries = input().split('!')


def urgent(word):
    if word not in groceries:
        groceries.insert(0, word)

command = input()

while command != "Go Shopping!":
    tolken = command.split(' ')
    comm = tolken[0]
    word = tolken[1]

    if comm == 'Urgent':
        urgent(word)


    elif comm == 'Unnecessary':
        if word in groceries:
            groceries.remove(word)

    elif comm == 'Correct':
        new_word = tolken[2]
        if word in groceries:
            index = groceries.index(word)
            groceries[index] = new_word

    elif comm == 'Rearrange':
        if word in groceries:
            groceries.remove(word)
            groceries.append(word)

    command = input()
print(', '.join(groceries))