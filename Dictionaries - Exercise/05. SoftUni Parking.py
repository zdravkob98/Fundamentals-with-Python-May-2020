n = int(input())

my_dict = {}

for i in range(n):
    tolken = input().split(' ')
    command = tolken[0]
    name = tolken[1]

    if command == 'register':
        number = tolken[2]
        if name in my_dict:
            print(f"ERROR: already registered with plate number {number}")
        else:
            my_dict[name] = number
            print(f"{name} registered {number} successfully")

    elif command == 'unregister':
        if name not in my_dict:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            my_dict.pop(name)

for key, value in my_dict.items():
    print(f'{key} => {value}')