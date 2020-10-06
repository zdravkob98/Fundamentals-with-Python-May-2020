data = input()
contests = {}
individual_statistics = {}

while data != 'no more time':
    data = data.split(' -> ')
    username = data[0]
    contest = data[1]
    points = int(data[2])
    if contest not in contests:
        contests[contest] = {username: points}
    else:
        if username not in contests[contest]:
            contests[contest][username] = points
        if contests[contest][username] < points:
            contests[contest][username] = points


    if username not in individual_statistics:
        individual_statistics[username] = {contest: points}
    else:
        if contest not in individual_statistics[username]:
                individual_statistics[username][contest] = points
        if individual_statistics[username][contest] < points:
                individual_statistics[username][contest] = points


    data = input()

for k,v in contests.items():
    print(f'{k}: {len(v)} participants')
    v = dict(sorted(v.items(), key=lambda x: (-x[1], x[0]) ))
    n = 1
    for k1,v1 in v.items():
        
        print(f'{n}. {k1} <::> {v1}')
        n += 1
print('Individual standings:')
n = 1
individual_statistics = dict(sorted(individual_statistics.items(), key=lambda x: (-sum(x[1].values()), x[0])))
for k2,v2 in individual_statistics.items():
    print(f'{n}. {k2} -> {sum(v2.values())}')
    n += 1
