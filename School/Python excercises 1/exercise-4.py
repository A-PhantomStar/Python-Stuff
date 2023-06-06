number = int(input('Enter a number of stones:\n>')) #We ask the user for an integer number of stones. we save the number on the variable.
list = [] #We declare an empty array.

for i in range(number): #We iterate through the range of the number.
    list.append(number) #We add the number on the list.
    number += 2 #We add two to the number.
print(list) #we print the list.