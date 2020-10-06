l1 = input().split(', ')
l2 = input()

contain_word = [word for word in l1 if word in l2]
print(contain_word)