command = input()

my_dict = {}

while command != 'Lumpawaroo':
    if '|' in command:
        tolken = command.split(' | ')
        side = tolken[0]
        user = tolken[1]

        if side not in my_dict:
            my_dict[side] = []

        if user not in my_dict[side]:
            my_dict[side].append(user)

    else:
        tolken = command.split(' -> ')
        t_user = tolken[0]
        t_side = tolken[1]

        if t_side not in my_dict:
            my_dict[t_side] = []

        flag = False

        for key, value in my_dict.items():
            if t_user in value:
                my_dict[key].remove(user)
                my_dict[t_side].append(t_user)
                print(f"{t_user} joins the {t_side} side!")
                flag = True


        if flag == False:
            my_dict[t_side].append(t_user)
            print(f"{t_user} joins the {t_side} side!")
            flag = True


    command = input()

my_dict = dict(sorted(my_dict.items(),key=lambda x: (-len(x[1]), x[0])))

for key, value in my_dict.items():
    if len(value) == 0:
        continue
    print(f'Side: {key}, Members: {len(value)}')

    for user in sorted(value):
        print(f'! {(user)}')
