import sys


def exchange(index_num, list_of_int_nums):
    first_half = list_of_int_nums[:index_num + 1]
    second_half = list_of_int_nums[index_num + 1:]
    list_of_int_nums = second_half + first_half
    return list_of_int_nums


def max_min_odd_even(command, list_of_int_nums):
    command = command.split(' ')
    min_max = command[0]
    odd_even = command[1]
    max_num = -sys.maxsize
    min_num = sys.maxsize
    idx = None
    found = False
    if min_max == 'max':
        if odd_even == 'odd':
            for i in range(len(list_of_int_nums) - 1, -1, -1):
                if int(list_of_int_nums[i]) % 2 != 0 and int(list_of_int_nums[i]) > max_num:
                    max_num = int(list_of_int_nums[i])
                    idx = i
                    found = True
        elif odd_even == 'even':
            for i in range(len(list_of_int_nums) - 1, -1, -1):
                if int(list_of_int_nums[i]) % 2 == 0 and int(list_of_int_nums[i]) > max_num:
                    max_num = int(list_of_int_nums[i])
                    idx = i
                    found = True
    elif min_max == 'min':
        if odd_even == 'odd':
            for i in range(len(list_of_int_nums) - 1, -1, -1):
                if int(list_of_int_nums[i]) % 2 != 0 and int(list_of_int_nums[i]) < min_num:
                    min_num = int(list_of_int_nums[i])
                    idx = i
                    found = True
        elif odd_even == 'even':
            for i in range(len(list_of_int_nums) - 1, -1, -1):
                if int(list_of_int_nums[i]) % 2 == 0 and int(list_of_int_nums[i]) < min_num:
                    min_num = int(list_of_int_nums[i])
                    idx = i
                    found = True
    if found:
        return idx
    elif not found:
        return 'No matches'


def first_even_odd(command, list_of_int_nums):
    command = command.split(' ')
    count = int(command[1])
    even_odd = command[2]
    first_nums = []
    valid = False
    if count == 0:
        return []
    elif count < 0:
        valid = False
    else:
        if even_odd == 'even':
            if count > len(list_of_int_nums):
                valid = False
            else:
                valid = True
                for i in list_of_int_nums:
                    if int(i) % 2 == 0:
                        first_nums.append(i)
                        count -= 1
                    if count == 0:
                        break
        elif even_odd == 'odd':
            if count > len(list_of_int_nums):
                valid = False
            else:
                valid = True
                for i in list_of_int_nums:
                    if int(i) % 2 != 0:
                        first_nums.append(i)
                        count -= 1
                    if count == 0:
                        break
    if not valid:
        return 'Invalid count'
    else:
        return list(map(int, first_nums))


def last_even_odd(command, list_of_int_nums):
    command = command.split(' ')
    count = int(command[1])
    even_odd = command[2]
    last_nums = []
    valid = False
    if count == 0:
        return []
    elif count < 0:
        valid = False
    else:
        if even_odd == 'even':
            if count > len(list_of_int_nums):
                valid = False
            else:
                valid = True
                for i in range(len(list_of_int_nums) - 1, -1, -1):
                    if int(list_of_int_nums[i]) % 2 == 0:
                        last_nums.append(list_of_int_nums[i])
                        count -= 1
                    if count == 0:
                        break
        elif even_odd == 'odd':
            if count > len(list_of_int_nums):
                valid = False
            else:
                valid = True
                for i in range(len(list_of_int_nums) - 1, -1, -1):
                    if int(list_of_int_nums[i]) % 2 != 0:
                        last_nums.append(list_of_int_nums[i])
                        count -= 1
                    if count == 0:
                        break
    if not valid:
        return 'Invalid count'
    else:
        last_nums.reverse()
        return list(map(int, last_nums))


integers_list = list(map(int, input().split(' ')))
manipulation = input()

while manipulation != 'end':
    if 'exchange' in manipulation:
        manipulation = manipulation.split(' ')
        index = int(manipulation[1])
        if index >= len(integers_list) or index < 0:
            print('Invalid index')
        else:
            integers_list = exchange(index, integers_list)
    elif 'max' in manipulation or 'min' in manipulation:
        print(max_min_odd_even(manipulation, integers_list))
    elif 'first' in manipulation:
        print(first_even_odd(manipulation, integers_list))
    elif 'last' in manipulation:
        print(last_even_odd(manipulation, integers_list))
    manipulation = input()

print(integers_list)