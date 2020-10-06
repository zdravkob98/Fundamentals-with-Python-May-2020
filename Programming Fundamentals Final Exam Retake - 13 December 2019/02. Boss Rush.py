import re

pattern = r'[|][A-Z]{4,}[|][:][#][A-Za-z]+[\s][A-Za-z]+[#]'

n = int(input())
for i in range(n):
    text = input()
    match = re.findall(pattern, text)

    if len(match) > 0:
        data = ':'.join(match)
        data = data.split(':')

        boss_name = data[0]
        boss = ''
        for char in boss_name:
            if char.isalpha():
                boss += char

        title_name = data[1]
        title = ''
        for char in title_name:
            if char.isalpha() or char == ' ':
                title += char

        print(f'{boss}, The {title}')
        print(f'>> Strength: {len(boss)}')
        print(f'>> Armour: {len(title)}')
    else:
        print("Access denied!")