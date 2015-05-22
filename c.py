def please_reverse (myarr):

    j = len(myarr) - 1
    k = 0
    a = len(myarr)/2

    while j >= a:
        temp = myarr[k]
        myarr[k] = myarr[j]
        myarr [j] = temp
        k = k+1
        j = j-1

    print (myarr)


myarr = [1, 2, 3, 6, 7]
please_reverse(myarr)

#
# ##j=3 k=0
# temp = 1
# arr[0] = 5
# arr[3] = 1
#
# k = 1
# j = 2
# temp=2
# arr[1]=3
# arr[2] = 2
# #k = 2
# #j = 1

###
