from pydoc import doc


characters = 'Bste!hetsi ogEAxpelrt x '
document = 'AlgoExpert is the Best!'

# function to return bool 
# if characters in characters string is enough to generate the characters in document string 

def generate_document(characters, document):
    # character_count dict to track unique characters and their respective count in characters
    character_count = {} 

    for character in characters:
        character_count[character] = character_count.get(character, 0) + 1
        # if character not in character_count:
        #     character_count[character] = 0
        # character_count[character] += 1

    for character in document:
        if character not in character_count or character_count[character] == 0:
            return False
        character_count[character] -= 1

    return True

can_document_generate = generate_document(characters=characters, document=document) 

print(can_document_generate)