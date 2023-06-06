askNum = True

def addNums():
    print("\n", numb1, "+", numb2, "=", numb1 + numb2)

def subsNums():
    print("\n", numb1, "-", numb2, "=", numb1 - numb2)

def multNums():
    print("\n", numb1, "*", numb2, "=", numb1 * numb2)

def divNums():
    print("\n", numb1, "/", numb2, "=", numb1 / numb2)

print("Welcome to the calculator!") 
while askNum == True:
    numb1 = float(input("\nPlease enter any number: \n>"))
    numb2 = float(input("Please enter another number: \n>"))
    print(numb1)
    print(numb2)
    choseOption = float(input("What do you want to do with this numbers?\n1)Add the two numbers.\n2)Substract the two numbers.\n3)Multiply the two numbers,\n4)Division of the numbers.\n5)Change the numbers.\n6)Turn off the calculator.\n>")) 
    if choseOption == 5:
        continue
    elif choseOption == 1:
        addNums()
    elif choseOption == 2:
        subsNums()
    elif choseOption == 3:
        multNums()
    elif choseOption == 4:
        if numb2 == 0:
            print("\nYou can't divide by zero! Please select another number.")
        else:    
            divNums()
    elif choseOption == 6:
        askNum = False

print("Exiting the calculator...")