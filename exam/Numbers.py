number = list(map(int, input().split()))

average = sum(number) / len(number)

greater_numbers = [n for n in number if n > average]
greater_numbers = sorted(greater_numbers, reverse=True)

top_5 = greater_numbers[:5]

top_5 = list(map(str, top_5))


if len(top_5) > 0:
    print(f"{' '.join(top_5)}")
else:
    print('No')