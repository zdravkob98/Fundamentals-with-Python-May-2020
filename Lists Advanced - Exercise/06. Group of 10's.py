import math
list_n = list(map(int, input().split(', ')))
max_n = max(list_n)
groups = math.ceil(max_n / 10)

for i in range(1 , groups + 1):
    current_list = []
    for n in list_n:
        if (i * 10) - 10 < n <= i * 10 :
            current_list.append(n)
    print(f"Group of {i * 10}'s: {current_list}")