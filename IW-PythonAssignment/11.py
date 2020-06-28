string = input("enter a sentence: ")
result = {}
for word in string.split(' '):
    if word in result:
        result[word] += 1
    else:
        result[word] = 1
print(result)