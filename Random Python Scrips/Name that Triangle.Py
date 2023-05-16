sideA = int(input("Please enter the value of side A\n>"))
sideB = int(input("Please enter the value of side B\n>"))
sideC = int(input("Please enter the value of side C\n>"))

if sideA == sideB and sideA == sideC:
    print("Your triangle is an Equilateral Triangle!")
else:
    if sideA == sideB or sideA == sideC or sideB == sideC:
        print("Your triangle is an Isosceles Triangle!")
    else:
        if sideA != sideB and sideA != sideC and sideB != sideC:
            print("Your triangle is an Scalene Triangle!")