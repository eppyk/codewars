def whatCentury(year):
    int(year)

    ending = year % 100
    year = (year - ending) / 100
    year = year + 1

    output = str(year) + "th"
    return output

bz = input("???   ")

whatCentury(bz)
