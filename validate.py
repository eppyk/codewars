def validate(n):

    if n==0:
        return True
    elif n < 10:
        return False

    array1 = map(int, str(n))
    length = len(array1)

    if length%2 == 0:

        for i in (0, length-1):
            doubled = array1[i]*2
            if doubled > 9:
                array1[i] = doubled%10 + 1
            i = i+2

    elif length%2 != 0:

        for i in (1, length-1):
            doubled = array1[i]*2
            if doubled > 9:
                array1[i] = doubled%10 + 1
            i = i+2

    array2 = map(int, array1)

    if sum(array2)%10==0:
        return True

    else:
        return False


print validate(10999)
