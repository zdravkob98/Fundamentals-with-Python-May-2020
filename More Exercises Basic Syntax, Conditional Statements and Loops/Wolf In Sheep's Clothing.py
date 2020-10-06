start = input()

user_list = start.split()

if user_list[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    user_list.reverse()
    print(f'Oi! Sheep number {user_list.index("wolf,") }! You are about to be eaten by a wolf!')
