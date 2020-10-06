import re

pattern = r'^[@][#]+[A-Z][A-Za-z0-9]{4,}[A-Z][@][#]+$'

n = int(input())

for i in range(n):
    product = input()
    match = re.findall(pattern, product)
    if len(match) > 0:

        group = ''
        for barcode in match:
            for ch in barcode:
                if ch.isdigit():
                    group += ch
        if len(group) == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {group}")

    else:
        print("Invalid barcode")
