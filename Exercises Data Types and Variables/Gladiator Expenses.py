lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price  = float(input())
armor_price  = float(input())

total = 0

for game in range(1 , lost_fights_count + 1):
    if game % 2 == 0:
        total += helmet_price
    if game % 3 == 0:
        total += sword_price
    if game % 6 == 0:
        total += shield_price
    if game % 12 == 0:
        total += armor_price
print(f"Gladiator expenses: {total:.2f} aureus")

