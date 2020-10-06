contests = {}
submissions = {}
data = input()

while data != "end of contests":
    tokens = data.split(':')
    contest = tokens[0]
    
    password = tokens[1]
    contests[contest] = password
    data = input()

while True:
    line = input()
    if line == "end of submissions":
        break
    line = line.split("=>")
    contest = str(line[0])
    password = str(line[1])
    username = str(line[2])
    points = int(line[3])

    if contest in contests and password == contests[contest]:
        if username not in submissions:
            submissions[username] = {contest: points}
        else:
            if contest not in submissions[username]:
                submissions[username][contest] = points
            if submissions[username][contest] < points:
                submissions[username][contest] = points


submissions = dict(sorted(submissions.items(), key=lambda x: (-sum(x[1].values()), x[0])))
for k, v in submissions.items():
    print(f'Best candidate is {k} with total {sum(v.values())} points.')
    break
print("Ranking:")
sorted_by_name = dict(sorted(submissions.items(), key=lambda x: x[0]))
for k, v in sorted_by_name.items():
    print(k)
    v = dict(sorted(v.items(), key=lambda x: -x[1]))
    for k2, v2 in v.items():
        print(f'#  {k2} -> {v2}')
