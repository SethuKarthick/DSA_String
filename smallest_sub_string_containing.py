def get_smallest_string_containing(big_string, small_string):
    target_char_counts = get_char_counts(small_string)
    sub_string_bounds = get_sub_string_bounds(big_string, target_char_counts)
    return get_string_from_bounds(big_string, sub_string_bounds)


def get_string_from_bounds(string, bounds):
    start, end = bounds
    if end == float('inf'):
        return ""
    return string[start:end+1]


def get_sub_string_bounds(string, target_char_counts):
    left_idx = 0
    right_idx = 0
    sub_string_bounds = [0, float('inf')]
    sub_string_char_counts = {}
    num_unique_char = len(target_char_counts.keys())
    num_unique_char_done = 0

    while right_idx < len(string):
        right_char = string[right_idx]
        if right_char not in target_char_counts:
            right_idx += 1
            continue
        increase_char_counts(right_char, sub_string_char_counts)
        if sub_string_char_counts[right_char] == target_char_counts[right_char]:
            num_unique_char_done += 1
        while num_unique_char_done == num_unique_char and left_idx <= right_idx:
            sub_string_bounds = get_closer_bounds(left_idx, right_idx, sub_string_bounds[0], sub_string_bounds[1])
            left_char = string[left_idx]
            if left_char not in target_char_counts:
                left_idx += 1
                continue
            if sub_string_char_counts[left_char] == target_char_counts[left_char]:
                num_unique_char_done -= 1
            decrease_char_counts(left_char, sub_string_char_counts)
            left_idx += 1
        right_idx += 1
    return sub_string_bounds

def get_closer_bounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]

def get_char_counts(string):
    char_counts = {}
    for char in string:
        increase_char_counts(char, char_counts)
    return char_counts




def increase_char_counts(char, char_counts):
    if char not in char_counts:
        char_counts[char] = 0
    char_counts[char] += 1

def decrease_char_counts(char, char_counts):
    char_counts[char] -= 1


smallest_sub_string = get_smallest_string_containing(big_string='abcd$ef$axb$c$', small_string='$$abf')
print(smallest_sub_string)