Numero = int(input("Ingrese un numero! \n >"))

for i in range(1,Numero+1,+1):
    print(i)

finalNumber = Numero * (Numero + 1) / 2

print("The result is ", round(finalNumber))
