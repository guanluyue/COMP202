#Name: Luyue Guan
#Student ID: 260950108

from algonquin_utils import *
def get_consonant_pronunciation(char):
    
    '''
    str -> str
    
    returns the pronunciation of a given consonant
    
    >>> get_consonant_pronunciation('d')
    'D'
    >>> get_consonant_pronunciation('j')
    'GE'
    >>> get_consonant_pronunciation('r')
    ''
    '''
    
    #convert into lowercase
    char = char.lower()
    #create a list of all the consonants
    consonants = ['b', 'c', 'd', 'g', 'h', 'k', 'm', 'n', 'p', 's', 't', 'w', 'y', 'z', 'j', 'dj']
    #create a list of corresponding pronunciation of each consonant
    consonant_pronunciation = ['B', 'C', 'D', 'G', 'H', 'K', 'M', 'N', 'P', 'S', 'T', 'W', 'Y', 'Z', 'GE', 'J']
    if is_valid_consonant(char) == False:
        return ''
    #get the index of the consonant and return its corresponding pronunciation in the other list
    return consonant_pronunciation[consonants.index(char)]

def get_vowel_pronunciation(char):
    
    '''
    str -> str
    
    returns the pronunciation of a given vowel
    
    >>> get_vowel_pronunciation('a')
    'A'
    >>> get_vowel_pronunciation('e')
    'E'
    >>> get_vowel_pronunciation('o')
    'U'
    '''
    
    #convert into lowercase
    char = char.lower()
    #create a list of all the vowels
    vowels = ['a', 'e', 'i', 'o', 'à', 'è', 'ì', 'ò']
    #create a list of corresponding pronunciation of each vowel
    vowel_pronunciation = ['A', 'E', 'I', 'U', 'A', 'E', 'EE', 'O']
    if is_valid_vowel(char) == False:
        return ''
    #get the index of the vowel and return its corresponding pronunciation in the other list
    return vowel_pronunciation[vowels.index(char)]

def get_diphthong_pronunciation(diphthong):
    
    '''
    str -> str
    
    returns the pronunciation of a diphthong

    >>> get_diphthong_pronunciation('ay')
    'EYE'
    >>> get_diphthong_pronunciation('ow')
    'OW'
    >>> get_diphthong_pronunciation('oy')
    ''
    '''
    
    #convert into lowercase
    diphthong = diphthong.lower()
    diphthong_pronunciation = ['OW', 'EYE', 'AO', 'AY', 'EW', 'OW']
    if diphthong not in DIPHTHONGS:
        return ''
    return diphthong_pronunciation[DIPHTHONGS.index(diphthong)]
    
    
def get_word_pronunciation(word):
    
    '''
    str -> str
    
    returns the pronunciation of a word
    
    >>> get_word_pronunciation('kwey')
    'KWAY'
    >>> get_word_pronunciation('madjashin')
    'MAJASHIN'
    >>> get_word_pronunciation('kasagiyan')
    'KASAGIYAN'
    '''
    #convert to lowercase
    word = word.lower()
    if is_valid_single_word(word) == True:
        #use an empty string to start with
        word_pronunciation = ''
        char = 0
        while char in range(len(word)):
            #check for character that can potentially form a diphthong with the next character
            if word[char] in ['a', 'e', 'i', 'o']:
                if word[char : char + 2] in DIPHTHONGS:
                    diphthong = word[char : (char + 2)]
                    word_pronunciation += get_diphthong_pronunciation(diphthong)
                    #add the pronunciation to the pronunciation string and skip the next character
                    char += 2
                    continue
                else:
                    word_pronunciation += get_vowel_pronunciation(word[char])
                    char += 1
                    continue
            elif word[char] == 'd':
                if word[char : char + 2] == 'dj':
                    word_pronunciation += 'J'
                    char += 2
                    continue
            #add the pronunciation of the remaining consonants and vowels
            char_pronunciation = get_vowel_pronunciation(word[char]) + get_consonant_pronunciation(word[char])
            word_pronunciation += char_pronunciation
            char += 1
        return word_pronunciation
    else:
        return ''
def tokenize_sentence(sentence):
    
    '''
    str -> str
    
    return the breakdown of a sentence into strings
    
    >>> tokenize_sentence('a test')
    ['a', ' ', 'test']
    >>> tokenize_sentence('just__@a# test!')
    []
    >>> tokenize_sentence('Kwey')
    ['Kwey']
    >>> tokenize_sentence('Kwey, anin eji-pimadizin?')
    ['Kwey', ', ', 'anin', ' ', 'eji', '-', 'pimadizin', '?']
    '''
    
    list_words = []
    word = ''
    if is_valid_phrase(sentence):
        for char in range(len(sentence)):
            if sentence[char] not in PUNCTUATION and sentence[char] != ' ':
                word += sentence[char]
                if char == (len(sentence) - 1):
                    list_words.append(word)
                    return list_words
                continue
            elif sentence[char] in PUNCTUATION or sentence[char] == ' ':
                if char < (len(sentence) - 1):
                    if sentence[char + 1] in PUNCTUATION or sentence[char + 1] == ' ':
                        list_words.append(word)
                        word = ''
                        list_words.append(sentence[char : char + 2])
                        continue
                    elif sentence[char - 1] in PUNCTUATION or sentence[char - 1] == ' ':
                        continue
                list_words.append(word)
                list_words.append(sentence[char])
                word = ''
                continue
            
        return list_words
    else:
        return []    
def get_sentence_pronunciation(sentence):
    
    '''
    str -> str
    
    return the pronunciation of a sentence
    
    >>> get_sentence_pronunciation('Kwey')
    'KWAY'
    >>> get_sentence_pronuncaition('Andi ejayan?')
    'ANDI EGEEYEAN?'
    >>> get_sentence_pronunciation('Mino ishkwa nawakwe')
    'MINU ISHKWA NOWAKWE'
    >>> get_sentence_pronunciation('I scream, you scream, we al scream for ice cream')
    ''
    '''
    list_words = tokenize_sentence(sentence)
    if list_words == []:
        return ''
    pronunciation = ''
    for word in list_words:
        if word in PUNCTUATION or word == ' ':
            pronunciation += word
            continue
        pronunciation += get_word_pronunciation(word)
    return pronunciation
tokenize_sentence('Kwey, anin eji-pimadizin?')     
