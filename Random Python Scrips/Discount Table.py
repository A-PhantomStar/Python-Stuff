pricesList = (4.95, 9.95, 14.95, 19.95, 24.95)
count = 1

for i in pricesList:
    print(f"Item #{count}:")
    print(f"Original price: ${i}")
    print("Discount: -60%")
    print(f"Price with discount: ${round(i * 0.4, 2)}\n")
    count += 1