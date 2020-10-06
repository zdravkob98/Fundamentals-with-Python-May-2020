
quantity = int(input())
days = int(input())

ornament_Set = 2
tree_Skirt = 5
tree_Garlands = 3
tree_Lights = 15

spirit = 0
budget = 0

for d in range(1 , days + 1):
    if d % 11 == 0:
        quantity += 2
    if d % 2 == 0 :
        budget += ornament_Set * quantity
        spirit += 5
    if d % 3 == 0:
        budget += (tree_Skirt + tree_Garlands ) * quantity
        spirit += 13
    if d % 5 == 0:
        budget += tree_Lights  * quantity
        if d % 5 == 0 and d % 3 == 0:
            spirit += 30
        else:
            spirit += 17
    if d % 10 == 0 :
        spirit -= 20
        budget += tree_Lights  + tree_Garlands  + tree_Skirt
if d % 10 == 0 :
    spirit -= 10
print(f'"Total cost: {budget}')
print(f'Total spirit: {spirit}')

