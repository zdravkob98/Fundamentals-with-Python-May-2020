def loading_bar(number):


    if number == 0:
        print(f'0% [..........]')
        print('Still loading...')

    elif number == 100:
        print(f'100% Complete!')
        print('[%%%%%%%%%%]')

    else:
        how_first_symbols_needed = number // 10
        firs_symbols = '%' * how_first_symbols_needed
        how_second_symbols_needed = 10 - how_first_symbols_needed
        second_symbols = '.' * how_second_symbols_needed

        print(f'{number}% [{firs_symbols}{second_symbols}]')
        print('Still loading...')


number = int(input())
loading_bar(number)