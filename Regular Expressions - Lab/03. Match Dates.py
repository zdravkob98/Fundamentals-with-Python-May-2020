import re

text = input()
pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'


for match in re.findall(pattern, text):
    day, _, month, year = match
    print(f'Day: {day}, Month: {month}, Year: {year}')
