record = {}
data = input()
while data != 'Log out':
    tolken = data.split(':')
    command = tolken[0]
    username = tolken[1]

    if command == 'New follower':
        if username not in record:
            record[username] = [0, 0]
    elif command == 'Like':
        count = int(tolken[2])
        if username not in record:
            record[username] = [0, 0]
        record[username][0] += count
    elif command == 'Comment':
        if username not in record:
            record[username] = [0, 0]
        record[username][1] += 1
    elif command == 'Blocked':
        if username not in record:
            print(f"{username} doesn't exist.")
        else:
            record.pop(username)
    data = input()

print(f'{len(record)} followers')
record = sorted(record.items(), key=lambda x: (-sum(x[1]), x[0]))
for k, v in record:
    print(f'{k}: {sum(v)}')