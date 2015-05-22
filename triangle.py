# Should print triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle
import math

def triangle_type(a, b, c):
    maxi = max(a,b,c)
    mini = min(a, b, c)
    midi = ((a+b+c)-(maxi+mini))
    
    if a+b>c and b+c>a and a+c>b:

        print mini, midi, maxi

        if math.sqrt(mini**2 + midi**2) < math.sqrt(maxi**2):
            print 1
        elif mini**2 + midi**2 == maxi**2:
            print 2
        elif math.sqrt(mini**2 + midi**2) > math.sqrt(maxi**2):
            print 3

    else:
        print 0


triangle_type(7,12,8)
