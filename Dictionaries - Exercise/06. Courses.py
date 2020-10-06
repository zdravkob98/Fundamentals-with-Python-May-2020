command = input()

my_dict = {}

while command != 'end':
    command = command.split(' : ')
    course = command[0]
    name = command[1]

    if course not in my_dict:
        my_dict[course] = []
    my_dict[course].append(name)

    command = input()

my_dict = dict(sorted(my_dict.items(), key= lambda x: -len(x[1])))


for key, value in my_dict.items():
    print(f"{key}: {len(value)}")
    for name in sorted(value):
        print(f'-- {name}')