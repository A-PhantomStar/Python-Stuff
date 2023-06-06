list1, list2, list3 = [19, 19, 15, 5, 3, 5, 5, 2],[19, 15, 15, 5, 3, 3, 5, 2],[19, 19, 5, 5, 5, 5, 5] #Declare the 3 list.
vari2, vari1 = 0, 0 #I declared variables to store how mani 19 and 5 are on a list.

def checkif (listused): #Here I made a function thats programed to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
    global vari2, vari1 #We add access to the global variables.
    vari2, vari1 = 0, 0 #We set the variables to 0 everytime we execute the function.
    for i in listused:
        if i == 19: #Here we check if the value of i is the same as 19.
            vari2 += 1 #Add 1 to the variable.
            continue
        elif i == 5: #Here we check if the value of i is the same as 5.
            vari1 += 1 #Add 1 to the variable.
        else:
            continue #If the element i from the array isn't either 19 0r 5, then the program continues and doesn't do anything.

checkif(list1) #We execute the function.
print (vari2 == 2 and vari1 >= 3) #We check if on list one there are exactly two 19 and three or more 5.
checkif(list2) #We execute the function.
print (vari2 == 2 and vari1 >= 3) #We check if on list one there are exactly two 19 and three or more 5.
checkif(list3) #We execute the function.
print (vari2 == 2 and vari1 >= 3) #We check if on list one there are exactly two 19 and three or more 5.
