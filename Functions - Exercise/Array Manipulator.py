def exchange(numbers, index):
    first = numbers[:index + 1]
    second = numbers[index + 1:]
    numbers = second + first
    return numbers


def max_even_index(numbers):
    import sys
    target = -sys.maxsize
    index_num = -1
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 2 == 0:
            if num >= target:
                target = num
                index_num = i
    if index_num == -1:
        print("No matches")
    else:
        print(index_num)


def max_odd_index(numbers):
    import sys
    target = -sys.maxsize
    index_num = -1
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 2 != 0:
            if num >= target:
                target = num
                index_num = i
    if index_num == -1:
        print("No matches")
    else:
        print(index_num)


def min_Even_index(numbers):
    import sys
    target = sys.maxsize
    index_num = -1
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 2 == 0:
            if num <= target:
                target = num
                index_num = i
    if index_num == -1:
        print("No matches")
    else:
        print(index_num)


def min_Odd_index(numbers):
    import sys
    target = sys.maxsize
    index_num = -1
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 2 != 0:
            if num <= target:
                target = num
                index_num = i
    if index_num == -1:
        print("No matches")
    else:
        print(index_num)


def first_count_even(numbers, count_element):
    l = []
    counter = 0
    if count_element > len(numbers) or count_element < 0:
        print("Invalid count")
        return
    else:
        for num in numbers:
            n = num
            if n % 2 == 0:
                counter += 1
                l.append(n)
                if counter == count_element:
                    break
    if l == []:
        print([])
    else:
        print(l)


def first_count_odd(numbers, count_element):
    l = []
    counter = 0
    if count_element > len(numbers) or count_element < 0:
        print("Invalid count")
        return
    else:
        for num in numbers:
            n = num
            if n % 2 != 0:
                counter += 1
                l.append(n)
                if counter == count_element:
                    break
    if l == []:
        print([])
    else:
        print(l)


def last_count_even(numbers, count):
    l = []
    counter = 0
    if count_element > len(numbers) or count_element < 0:
        print("Invalid count")
        return
    else:
        for i in range(len(numbers) - 1, -1, -1):
            num = numbers[i]
            if num % 2 == 0:
                counter += 1
                l.append(num)
                if counter == count_element:
                    break
    if l == []:
        print([])
    elif counter == 1:
        print(l)
    else:
        l_reversed = []
        for i in range(len(l) -1, -1, -1):
            l_reversed.append(l[i])
        print(l_reversed)


def last_count_odd(numbers, count):
    l = []
    counter = 0
    if count_element > len(numbers) or count_element < 0:
        print("Invalid count")
        return
    else:
        for i in range(len(numbers) - 1, -1, -1):
            num = numbers[i]
            if num % 2 != 0:
                counter += 1
                l.append(num)
                if counter == count_element:
                    break
    if l == []:
        print([])
    elif counter == 1:
        print(l)
    else:
        l_reversed = []
        for i in range(len(l) - 1, -1, -1):
            l_reversed.append(l[i])
        print(l_reversed)



items = input().split(' ')
numbers = []
for item in items:
    numbers.append(int(item))
text = input()

while text != 'end':
    command = text.split()

    if command[0] == 'exchange':
        index = int(command[1])
        if index > len(numbers) or index < 0:
            print("Invalid index")
        else:
            numbers = exchange(numbers, index)

    elif command[0] == 'max':
        if command[1] == 'even':
            max_even_index(numbers)
        elif command[1] == 'odd':
            max_odd_index(numbers)

    elif command[0] == 'min':
        if command[1] == 'even':
            min_Even_index(numbers)
        elif command[1] == 'odd':
            min_Odd_index(numbers)

    elif command[0] == 'first':
        count_element = int(command[1])
        if command[2] == 'even':
            first_count_even(numbers, count_element)
        elif command[2] == 'odd':
            first_count_odd(numbers, count_element)

    elif command[0] == 'last':
        count_element = int(command[1])
        if command[2] == 'even':
            last_count_even(numbers, count_element)
        elif command[2] == 'odd':
            last_count_odd(numbers, count_element)

    text = input()

print(numbers)