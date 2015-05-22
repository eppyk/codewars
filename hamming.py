def hamming(a,b):

    a = list(a)
    b = list(b)
    ham_dist = 0

    if len(a) > len(b):
        maxi = a
        mini = b
    else:
        maxi = b
        mini = a

    difference = len(maxi) - len(mini)

    i = 1
    while i != len(mini):
        if a[i] != b[i]:
            ham_dist = ham_dist + 1
        i = i + 1


    return ham_dist + difference

hamming("Bibka", "I love Momma")
