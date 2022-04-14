words = ['that', 'this', 'deed', 'is', 'a']

def cal_min_char(words):
    max_freq = {}

    for word in words:

        char_freq = get_char_freq(word)
        max_freq = update_freq(char_freq, max_freq)

    return min_char_list(max_freq)

# get freq count of each character in each word
def get_char_freq(word):
    char_freq = {}
    for char in word:
        char_freq[char] = char_freq.get(char, 0) + 1

    return char_freq

# update char_freq in max_freq if char_freq in word is greater than the char_freq in max_freq 
def update_freq(char_freq, max_freq):
    for char in char_freq:
        frequency = char_freq[char]

        if char in max_freq:
            max_freq[char] = max(frequency, max_freq[char])
        else:
            max_freq[char] = frequency

    return max_freq

# append all characters wrt to the frequency in max_freqency in single list. 
def min_char_list(max_freq):
    characters = []
    for char in max_freq:
        frequency = max_freq[char]

        for _ in range(frequency):
            characters.append(char)


    return characters


_min_char_list = cal_min_char(words=words)
print(_min_char_list)