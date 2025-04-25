def count_words(text):   # No parameter needed
    word_list = text.split(sep=None,maxsplit=-1)   # Don't need to add (sep=None,maxsplit=-1) as those are default parameters
    return len(word_list)

def character_count(text):
    lower_case = text.lower()
    character_dictionary = {}
    for char in lower_case:
        character_dictionary[char] = character_dictionary.get(char, 0) + 1
    return character_dictionary

def sort_on(dict):
    return dict["num"]

def sorted_character_count(character_dict):
    result = []
    for char, count in character_dict.items():
        result.append({"char": char, "num": count})
    result.sort(reverse=True, key=sort_on)
    return result
    