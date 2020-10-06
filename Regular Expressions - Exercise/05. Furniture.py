import re

#pattern = r'>>([A-Za-z]+)<<(\d+(.\d+))!(\d)+'
pattern = r'>>([A-Za-z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)'

text = input()


print('Bought furniture:')
total = 0

while text != 'Purchase':
    match = re.fullmatch(pattern,text)

    if match is None:
        text = input()
        continue

    print(match[1])
    price = float(match[2])
    quantity = int(match[4])
    total += price * quantity

    text = input()

print(f'Total money spend: {total:.2f}')