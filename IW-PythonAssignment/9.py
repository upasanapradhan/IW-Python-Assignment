def exchange_first_and_last_char():
    string = input("enter a string: ")
    first = string[0]
    last = string[-1]
    new_string = last + string[1:-1] + first
    print(new_string)


exchange_first_and_last_char()