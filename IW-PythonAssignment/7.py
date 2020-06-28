words_list = ['apple', 'remember', 'bald']
longest = 0
for word in words_list:
    if len(word) > longest:
            longest = len(word)
print(longest)