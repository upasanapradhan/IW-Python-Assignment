str1 = input("Enter string: ")
# length of string less than 2
if len(str1) < 2:
    print('Empty String')
#retrieve first and last 2 letters
else:
    for i in str1:
        result = str1[0:2] + str1[-2:]
    print(result)