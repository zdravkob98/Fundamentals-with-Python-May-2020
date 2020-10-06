first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
people_count = int(input())

hour = 0

while people_count > 0:
    hour += 1
    per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
    people_count -= per_hour
    if hour % 4 == 0:
        hour += 1

print(f'Time needed: {hour}h.')