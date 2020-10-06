n = int(input())

possitive = []
negative = []
for i in range(n):
    num = int(input())
    if num >= 0:
        possitive.append(num)
    else:
        negative.append(num)
print(possitive)
print(negative)
print(f'Count of positives: {len(possitive)}. Sum of negatives: {sum(negative)}')