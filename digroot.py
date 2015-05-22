def digital_root(n):

    if n < 10:
        return n
    else:
        factor = n%10
        n = n + digital_root((n - factor)/10)


digital_root(1299)
