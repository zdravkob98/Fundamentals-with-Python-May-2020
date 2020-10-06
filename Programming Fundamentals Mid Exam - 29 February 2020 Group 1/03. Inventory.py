journal = input().split(', ')

while True:
    command = input()
    if command == 'Craft!':
        break
    tolken = command.split(' - ')
    comm = tolken[0]
    word = tolken[1]

    if comm == 'Collect':
        if word in journal:
            continue
        else:
            journal.append(word)

    elif comm == 'Drop':
        if word in journal:
            journal.remove(word)

    elif comm == 'Combine Items':
        new = word.split(':')
        first = new[0]
        second = new[1]
        if first in journal:
            ind = journal.index(first)
            journal.insert(ind + 1,second)

    elif comm == 'Renew':
        if word in journal:
            journal.append(journal.pop(journal.index(word)))

print(', '.join(journal))