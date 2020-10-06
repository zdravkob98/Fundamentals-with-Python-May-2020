data = input()
players = {}

while data != 'Season end':
    if '->' in data:
        data = data.split(' -> ')
        player = data[0]
        position = data[1]
        skill = int(data[2])
        if player not in players:
            players[player] = {position: skill}
        else:
            if position not in players[player]:
                players[player][position] = skill
            if players[player][position] < skill:
                players[player][position] = skill

    else:
        data = data.split(' vs ')
        name1 = data[0]
        name2 = data[1]
        n1 = 0
        n2 = 0
        if name1 in players and name2 in players:
            for k,v in players[name1].items():
                if k in players[name2].keys():
                    if players[name1][k] > players[name2][k]:
                        n1 += 1
                    elif players[name1][k] < players[name2][k]:
                        n2 += 1
            if n1 > n2:
                players.pop(name2)
            elif n2 > n1:
                players.pop(name1)

    data = input()

players = dict(sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])))
for k,v in players.items():
    print(f'{k}: {sum(v.values())} skill')
    v = dict(sorted(v.items(), key=lambda x: (-x[1], x[0])))
    for k1,v1 in v.items():
        print(f'- {k1} <::> {v1}')