import re
patter = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

n = int(input())

for _ in range(n):
    text = input()
    match = re.findall(patter, text)
    if len(match) == 0:
        print("The message is invalid")
    else:
        sum = []
        for char in match[0][1]:

            sum.append(str(ord(char)))

        print(f"{match[0][0]}{':'} {' '.join(sum)}")