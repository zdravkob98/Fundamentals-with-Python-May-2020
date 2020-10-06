cards = input().split()
shuffles_count = int(input())

mid = len(cards) // 2

result =[]
for i in range(shuffles_count):
    res = []
    for i in range(mid):
        first_card = cards[i]
        second_card = cards[i + mid]
        res.append(first_card)
        res.append(second_card)
    cards = res
print(cards)
