def divisors(n):
    a = 1
    divisors = []
    count = 0

    while a <= n:
        if n%a==0:
            
            divisors.append(a)
            count = count + 1
            print(a)
        a = a + 1

    print (count, divisors)


b = int(input("Fdfsdfs"))
divisors(b)
