def repeat_string(word):
    return word * (len(word))


string = input().split()
result = ''
for word in string:
    result += repeat_string(word)

print(result)