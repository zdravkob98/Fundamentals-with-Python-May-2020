def ban_word(ban_words, text):
    for word in ban_words:
        while word in text:
            text = text.replace(word, '*' * len(word))
    return text

ban_words = input().split(', ')
text = input()

print(ban_word(ban_words, text))