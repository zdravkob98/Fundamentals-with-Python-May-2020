words = input().split()
searched = input()

palindrome = []
counter = 0
for word in words:
    if word == word[::-1]:
        palindrome.append(word)

counter = palindrome.count(searched)

print(palindrome)
print(f'Found palindrome {counter} times')