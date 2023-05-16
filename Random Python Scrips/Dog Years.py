def convertToDY():
    humanYears = int(input("Please enter the dog age in human years\n>"))
    if humanYears <= 0:
        print("please enter a valid age! (no negative numbers or letters)")
        convertToDY()
    else:
        if humanYears <= 2:
            dogYears = humanYears * 10.5
            print("Your dog age in dog years is:", dogYears)
        else:
            if humanYears > 2:
                dogYears = 21 + ((humanYears - 2)* 4 )
                print("Your dog age in dog years is:", dogYears)
convertToDY()