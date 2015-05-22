def number_of_occurrences(s, xs):
    length = len(xs)
    number = s
    i = 0
    count = 0

    while i != length:
        if xs[i]==number:
            count = count+1
        i = i+1
    return count


number_of_occurrences(2, [0,2,2,3])
