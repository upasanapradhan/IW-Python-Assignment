def multi(y):
    return lambda x: x * y


n1 = int(input("Enter a number to multiply: "))
number1 = multi(n1)
n2 = int(input("Enter a number to multiply: "))
print("The product is: ", number1(n2))