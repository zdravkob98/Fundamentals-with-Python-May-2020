text = input().split('#')
water = int(input())

effort = 0
total_fire = 0

print('Cells:')


for e in (text):
    element = e.split('=')
    level = element[0]
    grades = int(element[1])

    if water < grades:
        continue

    if level == 'High ':
        if grades >= 81 and grades <= 125:
            print(f' - {grades}')
            water -= grades
            effort += grades * 0.25
            total_fire += grades

    elif level == 'Medium ':
        if grades >= 51 and grades <= 80:
            print(f' - {grades}')
            water -= grades
            effort += grades * 0.25
            total_fire += grades

    elif level == 'Low ':
        if grades >= 1 and grades <= 50:
            print(f' - {grades}')
            water -= grades
            effort += grades * 0.25
            total_fire += grades

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
