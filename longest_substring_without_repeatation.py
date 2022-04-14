def find_longest_substring(str):
    longest = [0, 1]

    last_seen = {}
    start_idx = 0

    for index, char in enumerate(str):
        if char in last_seen:
            start_idx = max(start_idx, last_seen[char]+1)
        if longest[1] - longest[0] < index+1 - start_idx:
            longest[0] = start_idx
            longest[1] =  index+1
        last_seen[char] = index

    return str[longest[0]:longest[1]]

str = "clementiscap"

longest_sub_string = find_longest_substring(str=str)
print(longest_sub_string)
