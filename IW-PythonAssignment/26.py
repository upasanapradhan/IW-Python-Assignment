def insert_string(my_list, string):
    for i in range(len(my_list)):
        my_list[i] = string + str(my_list[i])
    return my_list


print(insert_string([1, 2, 3, 4], 'emp'))