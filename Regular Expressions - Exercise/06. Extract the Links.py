import re

text = input()
pattern = r'\bw{3}.[A-Za-z0-9]+(-[A-Za-z0-9]+)*\.[A-Za-z]+(\.[A-Za-z]+)*'

while text != '':
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match[0])
    text = input()