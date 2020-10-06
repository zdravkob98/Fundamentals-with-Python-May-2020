strings_list = input().split(', ')
numbers_list = list(map(lambda x: int(x), strings_list))

even_i = []

even_l = [index for index in range(len(numbers_list))if numbers_list[index] % 2 == 0]
print(even_l)

#for i in range(len(numbers_list)):
    #if numbers_list[i] % 2 == 0:
        #even_i.append(i)
#print(even_i)






