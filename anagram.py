def isAnagram(test, original):
    test = list(test)

    i = 0
    correct = 0

    while correct == 0:

        if test[i] in original:
            i = i + 1
        else:
            correct = 1

    if correct == 0:
        return True
    else:
        return False


isAna
