text = input()
coffe = 0
flag = True
while text != 'END':
    doing = text
    if doing == 'coding' or doing == 'cat' or doing == 'dog' or doing == 'movie':
        coffe += 1
    if doing == 'CODING' or doing == 'CAT' or doing == 'DOG' or doing == 'MOVIE':
        coffe += 2
    if coffe > 5:
        flag = False
        break
    text = input()

if flag == False :
    print('You need extra sleep')
else:
    print(coffe)