employee_first = int(input())
employee_second = int(input())
employee_third = int(input())
student_count = int(input())

total_per_hour = employee_first + employee_second + employee_third
time = 0

while True:

    if student_count <= 0:
        break
    else:
        student_count -= total_per_hour
        time += 1
    if time % 4 == 0:
        time += 1


print(f'Time needed: {time}h.')