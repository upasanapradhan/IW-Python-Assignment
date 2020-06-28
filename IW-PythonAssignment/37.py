dict1 = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50}
mul = 1
for value in dict1.values():
    mul = mul * value
print("Multiplication of all items is: ", mul)