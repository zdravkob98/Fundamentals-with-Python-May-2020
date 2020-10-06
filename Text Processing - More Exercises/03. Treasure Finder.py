key = list(map(int,input().split()))



while True:
    data = input()
    message = ''
    if data == 'find':
        break
    else:
        for i in range(len(data)):
            index = i % len(key) #key[index]
            help = ord(data[i]) - key[index]
            char = chr(ord(data[i]) - key[index])
            message += char

        type = ''
        number = ''
        name_flag = False
        age_flag = False

        for i in range(len(message)):
            char = message[i]
            if name_flag:
                type += message[i]
            if age_flag:
                number += message[i]
            if i < len(message) - 1 and name_flag == True or age_flag == True:

                if message[i + 1] == '&':
                    name_flag = False
                elif message[i + 1] == '>':
                    age_flag = False

            if message[i] == '&' and len(type) == 0 :
                name_flag = True
            elif message[i] == '<':
                age_flag = True
        print(f'Found {type} at {number}')