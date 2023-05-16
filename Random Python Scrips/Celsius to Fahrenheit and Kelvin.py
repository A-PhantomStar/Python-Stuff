tempC = int(input("Please enter the temperature in Celsius \n>"))

print("\nThe tempetature in Celsius is:", tempC, "°C")

def fahrenheit():
    tempF = tempC * 1.8 + 32
    print("The tempetature in Fahrenheit is:", tempF, "°F")

def Kelvin():
    tempK = tempC + 273.15
    print("The tempetature in Kelvin is:", tempK, "°K")

fahrenheit()
Kelvin()


