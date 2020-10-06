import re

destination = input()
pattern = r'(=|/)([A-Z][A-Za-z]{2,})\1'

match = re.findall(pattern, destination)
des = []
for m in match:
    des.append(m[1])

point = ''.join(des)
print(f"Destinations: {', '.join(des)}")
print(f'Travel Points: {len(point)}')