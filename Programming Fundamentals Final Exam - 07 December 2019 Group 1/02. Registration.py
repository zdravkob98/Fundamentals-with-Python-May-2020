import re

n = int(input())

pattern = r'[U][$]([A-Z][a-z]{2,})[U][$][P][@][$]([a-z]{5,}[0-9]+)[P][@][$]'
registration = 0

for _ in range(n):
    account = input()
    match = re.fullmatch(pattern, account)
    if match is None:
        print("Invalid username or password")
    else:
        registration += 1
        print("Registration was successful")
        print(f"Username: {match[1]}, Password: {match[2]}")
print(f"Successful registrations: {registration}")