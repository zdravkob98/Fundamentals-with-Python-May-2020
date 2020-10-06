command = input()

no_banned = {}
people = {}

while command != 'exam finished':
    if 'banned' in command:
        command = command.split('-')
        user_for_ban = command[0]
        if user_for_ban in people:
            del people[user_for_ban]

    else:
        command = command.split('-')
        name = command[0]
        language = command[1]
        point = int(command[2])

        if language not in no_banned:
            no_banned[language] = 0
        no_banned[language] +=1

        if name in people:
            if people[name] <= point:
                people[name] = point

        if name not in people:
            people[name] = {}
            people[name] = point


    command = input()

no_banned = dict(sorted(no_banned.items(), key=lambda x: (-x[1], x[0])))
people = dict(sorted(people.items(), key=lambda x: (-x[1], x[0])))

print('Results:')
for key, value in people.items():
    print(f'{key} | {value}')
print('Submissions:')
for key, value in no_banned.items():
    print(f'{key} - {value}')