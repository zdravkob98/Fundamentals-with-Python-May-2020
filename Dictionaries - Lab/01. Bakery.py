elements = input().split()

my_dict = {}

for element in range(0 , len(elements) , 2):
    my_dict[elements[element]] = int(elements[element + 1])

print(my_dict)