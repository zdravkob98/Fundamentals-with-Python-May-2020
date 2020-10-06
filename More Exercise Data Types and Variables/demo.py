line = int(input())

open = 0
close = 0
history = ''
flag = True
br = False

for i in range(line):
    char = input()
    if i == '(' and flag == False:
        print('UNBALANCED')
        br = True
        break
    if i == ')' and flag == True:
        print('UNBALANCED')
        br = True
        break

    if i == '(' and flag == True:
        open += 1
        flag = False
    if i == ')' and flag == False:
        close += 1
        flag = True

if br == False:
    if open == close:
        print('BALANCED')
    else:
        print('UNBALANCED')

