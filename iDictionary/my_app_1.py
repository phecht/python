'''
my_app_1.py is a definition finder from the definitons in data.json
'''
import json
from difflib import get_close_matches

ALL_WORDS = json.load(open("data.json"))

def acronym(words):
    return words.upper()

def proper_noun(words):
    ws = words.split()
    nouns = ""
    for w in ws:
        nouns = nouns + " " +  w[0].upper() + w[1:]
    return nouns.strip()

def find_word(search_word):
    """find_word finds a word and returns one or more definitons. """
    #Set it lower, make it proper and an ancronym
    search_word = search_word.lower()
    a_proper_noun = proper_noun(search_word)
    a_acronym = acronym(search_word)

    if search_word in ALL_WORDS:
        return ALL_WORDS[search_word]
    elif a_proper_noun in ALL_WORDS:
        return ALL_WORDS[a_proper_noun]
    elif a_acronym in ALL_WORDS:
        return ALL_WORDS[a_acronym]
    
    elif len(get_close_matches(search_word, ALL_WORDS.keys())) > 0:
        maybe_word = get_close_matches(search_word, ALL_WORDS.keys())[0]
        use_close = input( "Did you mean " + maybe_word + " instead?")
        if use_close.lower() =='y':
            return ALL_WORDS[maybe_word]
        else:
            return "We tried. Sorry" 
    else:
        return search_word + " was not found."

    

def main_loop():
    """The main_loop finds words until q is pressed. """
    A_WORD = input("Enter word:")
    THE_DEF = find_word(A_WORD)
    while A_WORD != 'q':
        if isinstance(THE_DEF, list):
            for item in THE_DEF:
                print(item)
        else:
            print(THE_DEF)
        A_WORD = input("Enter word:")
        THE_DEF = find_word(A_WORD)

main_loop()
