def factorial_division(first_num , second_num):

    factorial_first_number = first_num
    factorial_second_number = second_num

    for i in range(1 , first_num - 1):
        factorial_first_number *= (first_num - i)

    for i in range(1 , second_num - 1):
        factorial_second_number *= (second_num - i)

    print(f'{factorial_first_number / factorial_second_number:.2f}')


first_num = int(input())
second_num = int(input())

factorial_division(first_num , second_num)