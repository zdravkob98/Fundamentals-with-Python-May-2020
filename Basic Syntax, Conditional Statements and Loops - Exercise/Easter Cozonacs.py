budget = float(input())
price_for_flour_kg = float(input())
price_pack_egg = price_for_flour_kg * 0.75
price_milk_l = price_for_flour_kg * 1.25
milk_250_ml = price_milk_l / 4

price_for_one_cozonac = price_pack_egg + price_for_flour_kg + milk_250_ml

count_kozonac = 0
count_colored_eggs = 0

while budget > price_for_one_cozonac :
    budget -= price_for_one_cozonac
    count_kozonac += 1
    count_colored_eggs += 3
    if count_kozonac % 3 == 0:
        count_colored_eggs -= (count_kozonac - 2)

print(f'You made {count_kozonac} cozonacs! Now you have {count_colored_eggs} eggs and {budget:.2f}BGN left.')
