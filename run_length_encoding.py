
# input
string = 'AAAABBBBBBBBBBBCCCCCCDDDD'

# Expected output 
#! 4A8B6C4D

def run_length_encoding(string):
    current_run_length = 1
    encoded_string = []

    for i in range(1, len(string)):
        current_letter = string[i]
        previous_letter = string[i-1]

        if current_letter != previous_letter or current_run_length == 9:
            encoded_string.append(str(current_run_length))
            encoded_string.append(previous_letter)
            current_run_length = 0
        current_run_length += 1

    encoded_string.append(str(current_run_length))
    encoded_string.append(string[len(string)-1])

    print(''.join(encoded_string))


run_length_encoding(string=string)