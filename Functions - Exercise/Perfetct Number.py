def perfect_number(number):


    is_perfect = 0
    mid = number // 2

    for i in range(1, mid +1):
        if number % i == 0:
            is_perfect += i

    if is_perfect == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)
