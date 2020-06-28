string = input("enter comma separated sequence of words: ").split(",")
string = sorted(string)
print("Sorted: " + ','.join(string))