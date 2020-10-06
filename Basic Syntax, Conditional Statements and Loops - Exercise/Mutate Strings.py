first_str = input()
second_str = input()
new_str = ''
for i in range(len(second_str)):
    if first_str[i] != second_str[i]:
        new_str = second_str[:i+1] + first_str[i + 1:]
        print(new_str)