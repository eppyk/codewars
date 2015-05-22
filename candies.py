def candies(s):

    maxi = max(s)
    i = 0
    count = 0

    if len(s) < 2:
        return -1

    while i < len(s):
        difference = maxi - s[i]
        count = count + difference
        i = i + 1


    return count


print candies([1,3,5,7])
