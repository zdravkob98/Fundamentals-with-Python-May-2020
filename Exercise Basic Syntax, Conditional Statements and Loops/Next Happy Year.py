year = input()
year_as_int = int(year)+1
year = str(year_as_int)


while True:
    if len(year) == len(set(year)):
        print(year)
        break
    year_as_int += 1
    year = str(year_as_int)