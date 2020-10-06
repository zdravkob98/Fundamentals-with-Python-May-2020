index_start = int(input())
index_end = int(input())

for i in range(index_start , index_end +1):
    letter = chr(i)
    print(f'{letter}' , end =' ')