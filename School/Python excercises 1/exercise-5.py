list1, list2, list3, list4 = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde'], ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde'], ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew'], ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew'] #We add the diferent lists we are using.
tempvar = [] #We decalre an empty list.
tempvar2 = [] #We decalre an empty list.
def check(listused):#We make a function that checks if the nth-1 string is a proper substring of the nth string in a given list of strings.
    tempvar = []  #We set the list to 0 elements everytime we execute the function.
    tempvar2 = [] #We set the list to 0 elements everytime we execute the function.
    for i in listused:
        if i == (len(listused) -2): #If the element i from the used list is the same as the length from the array minus 2.
            tempvar = listused[i] #We store the second to last element from the used list on the variable.
        if i == (len(listused) -1): #If the element i from the used list is the same as the length from the array minus 1.
            tempvar2 = listused[i] #We store the last element from the used list on the variable.
        else: continue


check(list1)#We execute the function.
print(tempvar in tempvar2) #If the element from the first variable (which would be the second to last element from the used list) is the same as the second variable (which would be the last element from the used list), it prints true.
check(list2)#We execute the function.
print(tempvar in tempvar2) #If the element from the first variable (which would be the second to last element from the used list) is the same as the second variable (which would be the last element from the used list), it prints true.
check(list3)#We execute the function.
print(tempvar in tempvar2) #If the element from the first variable (which would be the second to last element from the used list) is the same as the second variable (which would be the last element from the used list), it prints true.
check(list4)#We execute the function.
print(tempvar in tempvar2) #If the element from the first variable (which would be the second to last element from the used list) is the same as the second variable (which would be the last element from the used list), it prints true.
