def reverse_word(string):

    string_list = string.split(' ')
    left_idx = 0
    right_idx = len(string_list)-1

    while left_idx < right_idx:
        string_list[left_idx], string_list[right_idx] = string_list[right_idx], string_list[left_idx]
        left_idx += 1
        right_idx -= 1

    return ' '.join(string_list)

reversed_string = reverse_word(string = 'The Best!   ')
print(reversed_string)


