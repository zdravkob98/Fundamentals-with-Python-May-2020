n = int(input())

snowball_snow2 = 0
snowball_time2 = 0
snowball_quality2 = 0
snowball_value2 = 0

for snowball in range(n):
    snowball_snow =int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow // snowball_time) ** snowball_quality
    if snowball_value > snowball_value2:
        snowball_snow2 = snowball_snow
        snowball_time2 = snowball_time
        snowball_quality2 = snowball_quality
        snowball_value2 = snowball_value
print(f'{snowball_snow2} : {snowball_time2} = {snowball_value2} ({snowball_quality2})')
