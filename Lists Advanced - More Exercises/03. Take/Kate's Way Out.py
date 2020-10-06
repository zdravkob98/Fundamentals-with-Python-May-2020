n = int(input())

count = 0
find_k = False
flag = True
r = 0

while n != r:
    r += 1
    read = input()

    if read == '######' and find_k == True:
        print("Kate cannot get out")
        flag = False
        break

    for element in read:

        if element == '#' and find_k == True:
            count += 1

        elif element == 'k':
            find_k = True

        elif element == ' ' and find_k == True:
            break



if flag == True:
    print(f"Kate got out in {count} moves")