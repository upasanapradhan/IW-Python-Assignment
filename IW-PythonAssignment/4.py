def char_swap(str1, str2):
    first_swap = str2[:2] + str1[2:]
    second_swap = str1[:2] + str2[2:]
    result = first_swap + ' ' + second_swap
    return result


print(char_swap('abc', 'xyz'))
