population = list(map(int, input().split(', ')))
min_wealth = int(input())

flag = False

for i in range(len(population)):

    sum_of_population = 0
    for num in population:
        sum_of_population += num
    if len(population) * min_wealth > sum_of_population:
        print('No equal distribution possible')
        flag = True
        break

    if population[i] < min_wealth:
        needed = min_wealth - population[i]
        for index in range(1,len(population) +1):
            if population[-index] - needed >= min_wealth:
                population[-index] -= needed
                population[i] += needed
                break


if flag == False:
    print(population)