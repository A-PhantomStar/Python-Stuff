n = int(input("Please enter a number \n>"))
print(n >= 100)

# operations with integers

print(3 + 4) #adds both numbers and then prints the result.

print(3 - 4) #substracts the second number from the first number and then prints the result.

print(3 * 4) #multiplies both numbers and then prints the result.

print(3 / 4) #divides the first number by the second number and then prints the result.

print(10 % 3) #divides the first number by the second number and then prints the the remainder from the division.

print(10 // 3) #adds both numbers and then prints the rounded result, which is rounded down to the nearest integer.

print(2 ** 3) #Takes the secund number and acts as an exponent for the first.

print(2 ** 3 + 3 - 7 / 1 // 4) #We have 2 exponent 3 that is: 8. Then we have 7 divided by 1 = -7. -7 divided by 4 with the result rounded: -1. Finally, we have 8+3-2 = 9. The result is printed.

# Operations with text strings

print("Hola " + "Python " + "¿Qué tal?") #It prints Hola Python ¿Qué tal?. The + between each set of strings its added so they can be printed togeter.


print("Hola " + str(5)) #This prints the word "Hello" folowed by the number 5. The thing here is that the 5 is taken as a string thanks to the str(). So it prints Hola 5

# mixed operations

print("Hola " * 5) #Multiplying a tring by a number prints the string the number of times that it was multiplyed. In this case, the word "Hola" will print 5 times.

print("Hola " * (2 ** 3)) #This starts by doing 2 exponential 3: 8. Then it multiplyes the string "Hola" making it print 8 times.

my_float = 2.5 * 2 #This assigns the value 5.0 to the variable my_float.

print("Hola " * int(my_float)) #This converts the variable my_float to an integer, then multiplies by the string "hola", making it print 5 times

### Comparative Operators ###

# operations with integers

print(3 > 4) #Checks if the left number is greater than the right number. Then it prints if its true or false.

print(3 < 4) #Checks if the left number is lower than the right number. Then it prints if its true or false.

print(3 >= 4) #Checks if the left number is greater or equal to the right number. Then it prints if its true or false.

print(4 <= 4) #Checks if the left number is lower or equal to the right number. Then it prints if its true or false.

print(3 == 4) #Checks if both numbers are the same. Then it prints if its true or false.

print(3 != 4) #Checks if both numbers aren't the same. Then it prints if its true or false.

# Operations with text strings

print("Hola" > "Python") #Checks if the left string has more characters than the right one. It aslo takes on consideration the ASCII values when comparing. Then it prints if its true or false.

print("Hola" < "Python") #Checks if the left string has less characters than the right one. It aslo takes on consideration the ASCII values when comparing. Then it prints if its true or false.

print("aaaa" >= "abaa")  #This checks if the righ and left string has more or the same amount of characters. But it aslo takes on consideration the ASCII values when comparing.

print(len("aaaa") >= len("abaa"))  #Checks if the left string has less characters than the right one.

print("Hola" <= "Python") #Checks if the left string has less or the same characters than the right one. It aslo takes on consideration the ASCII values when comparing. Then it prints if its true or false.

print("Hola" == "Hola") #Checks if the left variable and the right variable are exatly the same.

print("Hola" != "Python") #Checks if the left variable and the right variable are  not exactly the same.



### Logical operators ###

# Based on Boolean Algebra https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole

print(3 > 4 and "Hola" > "Python") #this checks if both conditions are true, and only if both of them are true, then it prints true. In this case, both are false so it prints false.

print(3 > 4 or "Hola" > "Python") #this checks if both conditions are true, and if only one of them or both of them are true, then it prints true.  In this case, both are false so it prints false.

print(3 < 4 and "Hola" < "Python") #this checks if both conditions are true, and only if both of them are true, then it prints true. In this case, both of them are true so it prints true.

print(3 < 4 or "Hola" > "Python") #this checks if both conditions are true, and if only one of them or both of them are true, then it prints true. In this case, only one of them its true but it still prints true.

print(3 < 4 or ("Hola" > "Python" and 4 == 4)) #This starts inside the parenthesis, were we check both conditions are true to then compare the asnwer to the other condition outside, and if only one of them or both of them are true, then it prints true. Here, inside the parenthesis is false (since only one of them is true and the other is false), but the console only prints true since the one outside the parenthesis is true.

print(not (3 > 4)) #This checks if the condition is not true. If 3 isn't greater than 4, then it prints true.
