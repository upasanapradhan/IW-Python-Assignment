def count_string(my_list):
    count = 0
    for item in my_list:
        if len(item) >= 2:
            if item[0] == item[-1]:
                count += 1
    return count


print(count_string(['abc', 'xyz', 'aba', '1221']))
print(count_string(['aba', 'xyx', 'aba', '1221']))