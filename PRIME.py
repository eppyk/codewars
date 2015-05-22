import math

def is_prime(n):
    if n == 2:
       return True
    if n % 2 == 0 or n<=1:
        return False

    i = 3
    sqrtOfNumber = math.sqrt(n)

    while i <= sqrtOfNumber:
        if n % i == 0:
            return False
        i = i+2

    return True  
