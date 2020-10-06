list_of_emploees_happiness = list(map(int , input().split()))
happiness_improvement_factor = int(input())

increase_happiness = [n * happiness_improvement_factor for n in list_of_emploees_happiness]

filtered_happines = list(filter(lambda x: x >= sum(increase_happiness)/ len(increase_happiness), increase_happiness))

if len(filtered_happines) >= len(increase_happiness)/2 :
    print(f'Score: {len(filtered_happines)}/{len(increase_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(filtered_happines)}/{len(increase_happiness)}. Employees are not happy!')

