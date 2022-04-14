# input
string = 'noon'

# output 
# xyzzyx

def find_longest_palindrome(string):
    current_long = [0, 1]
    for i in range(1, len(string)):
        odd = helper(string, i-1, i+1)
        even = helper(string, i-1, i)
        longest = max(odd, even, key = lambda x : x[1] - x[0])
        current_long = max(longest, current_long, key= lambda x : x[1] - x[0])
    return string[current_long[0]: current_long[1]]
    

def helper(string, left_idx, right_idx):
    while left_idx >=0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1

    return [left_idx+1, right_idx] 


longeset_palindormic_sub_string = find_longest_palindrome(string=string)
print(longeset_palindormic_sub_string)
