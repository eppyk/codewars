def powerof4(n):

    if type(n) is int:

        power = 1
        while n > 4**power:
            power = power + 1

        if n==4**power:
            return True
        else:
            return False
    else:
        return False


print powerof4(16)
