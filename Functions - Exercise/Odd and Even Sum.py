number = input()


def odd_and_even_sum(number):
    even = 0
    odd = 0

    for i in range(len(number)):
        int_num = int(number[i])
        if int_num % 2 == 0:
            even += int_num
        else:
            odd += int_num

    print(f'Odd sum = {odd}, Even sum = {even}')


odd_and_even_sum(number)