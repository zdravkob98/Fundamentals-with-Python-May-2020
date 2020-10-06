str_one = input()
str_two = input()

for i in str_one:
    if str_one[i] != str_two[i]:
        for index in str_one:
            print(index)