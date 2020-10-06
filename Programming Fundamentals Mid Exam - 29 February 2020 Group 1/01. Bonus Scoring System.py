students_count = int(input())
lectures_count = int(input())
bonus = int(input())

import math

import sys

total = 0
attendances = 0

for i in range(students_count):
    student_attendances = int(input())
    total_bonus = math.ceil(( student_attendances / lectures_count) * (5 + bonus))

    if total_bonus >= total:
        total = total_bonus
        attendances = student_attendances

print(f"Max Bonus: {math.ceil(total)}.")
print(f"The student has attended {attendances} lectures.")