import re

pattern = r'[*]{2}[A-Z][a-z]{2,}[*]{2}|[:]{2}[A-Z][a-z]{2,}[:]{2}'
pattern2 = r'[0-9]'
data = input()

matches = re.findall(pattern, data)

threshold = 1
match_digits = re.findall(pattern2, data)
for digit in match_digits:
    threshold *= int(digit)


print(f'Cool threshold: {threshold}')
print(f'{len(matches)} emojis found in the text. The cool ones are:')

word_cool_threshold = 0
for match in matches:
    for char in match[2:-2]:
        word_cool_threshold += ord(char)
    if word_cool_threshold >= threshold:
        print(match)
        word_cool_threshold = 0