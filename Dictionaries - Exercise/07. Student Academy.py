n = int(input())

my_dict = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in my_dict:
        my_dict[name] = []
    my_dict[name].append(grade)

new_dict = {}

for key, value in my_dict.items():
    average = sum(value) / len(value)
    if average >= 4.5:
        new_dict[key] = average


new_dict = dict(sorted(new_dict.items(), key=lambda x: -x[1]))
for key, value in new_dict.items():
    print(f'{key} -> {value:.2f}')
