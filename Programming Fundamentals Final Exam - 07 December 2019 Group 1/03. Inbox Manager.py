my_dict = {}

data = input()
while data != 'Statistics':
    tolken = data.split('->')
    command = tolken[0]
    username = tolken[1]

    if command == 'Add':
        if username in my_dict:
            print(f"{username} is already registered")
        else:
            my_dict[username] = []
    elif command == 'Send':
        email = tolken[2]
        my_dict[username].append(email)
    elif command == 'Delete':
        if username in my_dict:
            my_dict.pop(username)
        else:
            print(f"{username} not found!")
    data = input()


print(f'Users count: {len(my_dict)}')

my_dict = sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0]))

for k, v in my_dict:
    print(k)
    for v1 in v:
        print(f"- {v1}")