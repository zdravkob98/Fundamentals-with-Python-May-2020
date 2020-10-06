def word_in_string(word, string):
    while repeated_word in string:
        string = string.replace(repeated_word, '')
    return string


repeated_word = input()
string = input()

print(word_in_string(repeated_word, string))
