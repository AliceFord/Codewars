# A program to find out which century a given year is in

year = 1800

def century(year):

    century = (year // 100) + 1

    if year / 100 == year // 100:
        century = year // 100

    return century


print(century(year))
