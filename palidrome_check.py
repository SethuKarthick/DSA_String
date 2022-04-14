


string = "abcdcba"

def is_palidrome(string):
    reversed_string = ""

    for i in reversed(range(len(string))):
        reversed_string += string[i]

    print(reversed_string == string)

# is_palidrome(string=string)


# without constants

def palindrome_check(string):
    left_idx = 0
    right_idx = len(string)-1

    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True 

is_string_palidrome = palindrome_check(string=string)
print(is_string_palidrome)