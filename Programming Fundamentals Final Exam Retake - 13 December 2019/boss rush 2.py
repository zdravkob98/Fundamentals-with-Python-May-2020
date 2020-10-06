import re
pattern = r'[|]([A-Z]{4,})[|][:][#]([A-Za-z]+[\s][A-Za-z]+)[#]'

n = int(input())

for i in range(n):
    text = input()
    match = re.findall(pattern, text)
    if len(match) > 0:
        #print(match[0][1])
        for words in match:
            print(f'{words[0]}, The {words[1]}')
            print(f'>> Strength: {len(words[0])}')
            print(f'>> Armour: {len(words[1])}')

    else:
        print("Access denied!")