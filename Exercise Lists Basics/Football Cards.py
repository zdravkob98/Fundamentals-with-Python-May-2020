cards = input().split()

team_a = [1] * 11
team_b = [1] * 11

for i in cards:
    red_card = i.split('-')

    team = red_card[0]
    player = int(red_card[1])

    if team == 'A':
        team_a[player - 1] = 0
    elif team == 'B':
        team_b[player - 1] = 0

print(f"Team A - {team_a.count(1)}; Team B - {team_b.count(1)}")

if team_a.count(1) < 7 or team_b.count(1) < 7:
    print("Game was terminated")