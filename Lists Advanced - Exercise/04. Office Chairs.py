rooms_n = int(input())
flag = True
free_chairs = 0

for room in range(1, rooms_n +1):
    chairs_in_room = input().split()
    chairs_needed = len(chairs_in_room[0])
    people_in_room = int(chairs_in_room[1])
    if chairs_needed < people_in_room:
        print(f"{people_in_room - chairs_needed} more chairs needed in room {room}")
        flag = False
    else:
        if chairs_needed > people_in_room:
            free_chairs += chairs_needed - people_in_room

if flag:
    print(f"Game On, {free_chairs} free chairs left")
