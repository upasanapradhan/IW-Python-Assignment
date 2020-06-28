str1 = input("enter a string: ")
if len(str1) >= 3:
    for i in str1:
        if 'ing' in str1:
            result = str1 + 'ly'
        else:
            result = str1 + 'ing'
    print(result)

else:
    print(str1)