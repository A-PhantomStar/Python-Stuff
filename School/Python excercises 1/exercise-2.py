list1, list2, list3, list4 = [19, 19, 15, 5, 5, 5, 1, 2], [19, 15, 5, 7, 5, 5, 2], [11, 12, 14, 13, 14, 13, 15, 14], [19, 15, 11, 7, 5, 6, 2] #Declare the 3 list.
vari1 = 0 #This stores how many times the fifth number repeats on a list.
numberfiv = 0 #This stores the fifth number from the selected list.
def checkif (listused): #Here is a function that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
    global vari2, vari1 #We add access to the global variables.
    vari1 = 0 #We set the variable to 0 everytime we execute the function.
    numberfiv = listused[4] #We set this variable to the fifth element from the list given.
    for i in listused:
        if i == numberfiv: #We check if the element i from the list is the same as the fifth element from the list.
            vari1 += 1 #We add one to the variable that counts how many times the fifth number appears on the list.
        else:
            continue #If the element i from the array isn't the same as the fifth number, then the program continues and doesn't do anything.

checkif(list1) #We execute the function.
print (vari1 == 3 and len(list1) == 8) #We check if the number 5 appears exactly 3 times, and also if the list has exatly 8 elements.
checkif(list2) #We execute the function.
print (vari1 == 3 and len(list2) == 8) #We check if the number 5 appears exactly 3 times, and also if the list has exatly 8 elements.
checkif(list3) #We execute the function.
print (vari1 == 3 and len(list3) == 8) #We check if the number 5 appears exactly 3 times, and also if the list has exatly 8 elements.
checkif(list4) #We execute the function.
print (vari1 == 3 and len(list4) == 8) #We check if the number 5 appears exactly 3 times, and also if the list has exatly 8 elements.