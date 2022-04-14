
# input
string = 'abcbcaf'

# output
# return the index of first non repeating character from string 
# else return -1

def find_non_repeating_character(string):
    character_freq = {}

    for character in string:
        character_freq[character] = character_freq.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if character_freq[character] == 1:
            return idx
        
    return -1

non_repeating_idx = find_non_repeating_character(string=string)
print(non_repeating_idx)