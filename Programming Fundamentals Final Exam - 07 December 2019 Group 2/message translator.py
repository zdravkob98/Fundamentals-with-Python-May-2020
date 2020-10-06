import re
patter = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

n = int(input())

for _ in range(n):
    text = input()
    match = re.fullmatch(patter, text)
    if match is None:
        print("The message is invalid")
    else:
        sum = []
        for char in match[2]:
            sum.append(str(ord(char)))
        print(f"{match[1]}{':'} {' '.join(sum)}")
