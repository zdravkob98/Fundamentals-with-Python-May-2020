word: str = input()
n: int = int(input())


def n_times_word (word , n):
    resut = ''
    resut = word * n
    return resut


print(n_times_word(word,n))