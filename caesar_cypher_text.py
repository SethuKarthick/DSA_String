# input 
string = 'zab'

key = 54

# outout --> 'bce'

alphabet = list('abcedfghijklmnopqrstuvwxyz')

def caesar_cypher_text(string, key):
    new_letters_string = []
    new_key = key % 26
    for letter in string:
        new_letters_string.append(get_new_letter(letter, new_key, alphabet))
    print(''.join(new_letters_string))


def get_new_letter(letter, key, alphabet):
    new_letter_key = alphabet.index(letter) + key
    return alphabet[new_letter_key % 26]


caesar_cypher_text(string=string, key=key)