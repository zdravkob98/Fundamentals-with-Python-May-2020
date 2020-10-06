n = int(input())
counter = 1
electrons_l = []

while n > 0:
    electrons =  2 * counter ** 2
    if electrons > n :
        electrons_l.append(n)
    else:
        electrons_l.append(electrons)
    n -= electrons
    counter += 1
print(electrons_l)