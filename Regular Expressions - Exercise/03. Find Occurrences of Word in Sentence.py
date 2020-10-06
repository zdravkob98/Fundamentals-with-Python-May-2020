import re

text = input()
key = input()
pattern = rf'\b{key}\b'

matches = re.findall(pattern, text, re.IGNORECASE)
print(len(matches))