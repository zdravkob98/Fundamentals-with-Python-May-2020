from _collections import defaultdict

my_dict = defaultdict(list)

n = int(input())

for i in range(n):
    word = input()
    synonym = input()
    my_dict[word].append(synonym)

for word, synonym in my_dict.items():
    normalized_synonym = ', '.join(synonym)
    print(f'{word} - {normalized_synonym}')
