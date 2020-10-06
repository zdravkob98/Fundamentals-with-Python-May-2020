#def reverse_string(word):
    #new_word = word[::-1]
    #return new_word

#def reverse_string(word):
    #new_word = list(reversed(word))
    #return ''.join(new_word)
    
while True:
    word = input()
    if word == 'end':
        break
    else:
        print(f"{word} = {reverse_string(word)}")