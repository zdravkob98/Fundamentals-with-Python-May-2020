line = int(input())

open = 0
close = 0
history = ''
flag = True
br = False

for i in range(line):
    char = input()
    if char == history:
        print('UNBALANCED')
        br = True
        break

    if char == '(' and flag == True:
        open += 1
        flag = False
        history = char
    if char == ')' and flag == False:
        close += 1
        flag = True
        history = char

if br == False:
    if open == close:
        print('BALANCED')
    else:
        print('UNBALANCED')