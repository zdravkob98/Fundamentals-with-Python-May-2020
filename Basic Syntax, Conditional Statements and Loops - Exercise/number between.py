divisor = int(input())
bound = int(input())

for n in range(bound, 0 , -1):
    if n % divisor == 0 and n <= bound:
        print(n)
        break