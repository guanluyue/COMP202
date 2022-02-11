#Name: Luyue Guan
#Student ID: 260950108

#Define the global variables
CONSONANTS = 'bcdghkmnpstwyzj'
VOWELS = 'aeio'
VOWELS_WITH_ACCENT = 'àèìò'
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']

def is_valid_consonant(char):
    '''
    (str) --> bool
    
    returns if the given character represents a valid consonant in Algonquin
    
    >>> is_valid_consonant('j')
    True
    >>> is_valid_consonant('l')
    False
    >>> is_valid_consonant('G')
    True
    >>> is_valid_consonant('hi')
    Please enter a valid character
    '''
    
    #Check if the input is valid
    if type(char) != str:
        print('Please enter a valid character')
        return
    elif len(char) > 1:
        return False
    #Convert the string into lowercase and check if it's one of the consonants
    return char.lower() in CONSONANTS
    #lowerchar = char.lower()
    #for i in range(len(lowerchar)):
        #return lowerchar[i] in CONSONANTS

def is_valid_vowel(char):
    '''
    (str) --> bool
    
    returns if the given character represents a valid vowel in Algonquin
    
    >>> is_valid_vowel('a')
    True
    >>> is_valid_vowel('ai')
    False
    >>> is_valid_vowel('h')
    False
    '''
    
    #Check if the input is valid
    if type(char) != str:
        print('Please enter a valid character')
        return
    elif len(char) > 1:
        return False
    #Convert the string into lowercase and check if it's one of the vowels
    return char.lower() in VOWELS or char.lower() in VOWELS_WITH_ACCENT

def is_valid_single_word(word):
    
    '''
    str --> bool
    
    returns if it contains a single word made up by valid letters in Algonquin
    
    >>> is_valid_single_word('Kwey')
    True
    >>> is_valid_single_word('rats')
    False
    >>> is_valid_single_word('ay, dj')
    False
    '''
    
    word = word.lower()
    for i in word:
        if i not in CONSONANTS + VOWELS + VOWELS_WITH_ACCENT and i not in DIPHTHONGS:
            return False
    return True

def is_valid_phrase(phrase):
    
    '''
    str -> bool
    
    returns if it only contains valid letters, punctuation or space in Algonquin
    
    >>> is_valid_phrase('Kwey')
    True
    >>> is_valid_phrase('Andi ejayan?')
    True
    >>> is_valid_phrase('I scream, you scream, we all scream for ice cream')
    False
    '''
    phrase = phrase.lower()
    for char in phrase:
        if char in CONSONANTS:
            continue
        elif char in VOWELS:
            continue
        elif char in VOWELS_WITH_ACCENT:
            continue
        elif char in PUNCTUATION:
            continue
        elif char == ' ':
            continue
        else:
            return False
    return True
    
 
    
    
    
    
    
    
    

    
