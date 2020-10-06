import re

text = input()
pattern = r'\d+'

while text != '':
    command = text
    matches = re.findall(pattern, text)
    for match in matches:
        print(match, end=' ')
    text = input()