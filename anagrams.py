# input 
words = ['yo', 'flop', 'cat', 'act', 'foo', 'tac', 'olfp']

def group_anagrams(words):
    anagrams = {}

    for word in words:
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())

grouped_anagrams = group_anagrams(words=words)
print(grouped_anagrams)