race = list(map(float, input().split()))
if len(race) % 2 == 1:
    finals = int((len(race) - 1 ) / 2)

def left(race, finals):
    time_1 = 0
    for i in range(finals):
        if race[i] == 0:
            time_1 *= 0.8
        time_1 += race[i]
    return time_1


def right(race, finals):
    time_2 = 0
    for i in range(finals + 1, len(race), 1):
        time_2 += race[i]
        if race[i] == 0:
            time_2 *= 0.8
    return time_2


first = left(race,finals)
second = right(race,finals)

if first < second:
    print(f"The winner is left with total time: {left(race, finals)}")
elif first > second:
    print(f"The winner is right with total time: {right(race, finals)}")
else:
    print("The winner is {left/right} with total time: {total time}")

#race = list(map(float, input().split()))
#if len(race) % 2 == 1:
#    finals = int((len(race) - 1 ) / 2)

#time_1 = 0
#for i in range(finals):
#    if race[i] == 0:
#        time_1 *= 0.8
#    time_1 += race[i]

#time_2 = 0
#for i in range(finals + 1, len(race), 1):
#    time_2 += race[i]
#    if race[i] == 0:
#        time_2 *= 0.8

#if time_1 < time_2:
#    print(f"The winner is left with total time: {time_1:.1f}")
#elif time_1 > time_2:
#    print(f"The winner is right with total time: {time_2:.1f}")