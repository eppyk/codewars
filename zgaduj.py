
print("Wymyśl liczbę z przedziału 1 do 1000.")
min = 1
max = 1000
guess = False


while guess==False:
    a = input("Is that number bigger or smaller than %s? \n" %(max/2))
    if a=="bigger":
        print(max)
        min = max/2

    elif a=="smaller":
        max = max/2
