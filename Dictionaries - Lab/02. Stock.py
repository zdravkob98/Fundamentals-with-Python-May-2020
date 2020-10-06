elements = input().split()
searched_element = input().split()

dict_elements = {}

for i in range(0, len(elements), 2):
    dict_elements[elements[i]] = elements[i + 1]

for i in range(len(searched_element)):
    if searched_element[i] in dict_elements.keys():
        print(f"We have {dict_elements[searched_element[i]]} of {searched_element[i]} left")
    else:
        print(f"Sorry, we don't have {searched_element[i]}")