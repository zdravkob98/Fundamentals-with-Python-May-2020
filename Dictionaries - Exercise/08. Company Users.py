command = input()

my_dict = {}

while command != 'End':
    tolken = command.split(' -> ')
    company = tolken[0]
    id = tolken[1]

    if company not in my_dict:
        my_dict[company] = []


    if id not in my_dict[company]:
        my_dict[company].append(id)


    command = input()

my_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
for key, value in my_dict.items():
    print(f'{key}')
    for id in value:
        print(f'-- {id}')