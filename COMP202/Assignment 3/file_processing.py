#Name: Gwen Guan
#Student ID: 260950108
import doctest
from similarity_measures import *
def get_sentences(s):
    '''
    str -> list
    
    returns a list of strings representing one of the each sentence from the input
    
    >>> text = 'Hello darkness my old friend. I have come to talk with you again.'
    >>> get_sentences(text)
    ['Hello darkness my old friend', 'I have come to talk with you again']
    
    >>> text = 'Hello'
    >>> get_sentences(text)
    ['Hello']
    
    >>> text = 'Bap beep boop? Beep bap boom!'
    >>> get_sentences(text)
    ['Bap beep boop', 'Beep bap boom']
    '''
    
    #first replace all punctuations with '.'
    new_text = s
    for char in s:
        if char in ['?','!']:
            new_text = new_text.replace(char, '.')
    #then split the string with '.'
    list_sentences = new_text.split('.')
    sentences = []
    for s in list_sentences:
        if s == '':
            continue
        #remove spaces following the punctuations in a sentence
        sentence = s.strip()
        sentences.append(sentence)
    return sentences

def get_word_breakdown(s):
    '''
    str -> list
    
    returns a 2D list of strings with each sublist contains strings representing words
    
    >>> get_word_breakdown('Hello')
    [['hello']]
    >>> get_word_breakdown('abc-def, ghi! "beep"')
    [['abc', 'def', 'ghi'], ['beep']]
    >>> get_word_breakdown('first line.\nsecond line')
    [['first', 'line'], ['second', 'line']]
    
    '''
    s = s.lower()
    #first get a list of sentences
    list_sentences = get_sentences(s)
    new_sentence = ''
    list_words = []
    #iterate through all lists of sentences and replace all punctuations with space
    for sentence in list_sentences:
        new_sentence = sentence
        for char in sentence:
            if char in ['-', '"', ',', ':', ';', '\'', '\n', '\t']:
                new_sentence = new_sentence.replace(char, ' ')
        list_words.append(new_sentence.split())
    return list_words

def build_semantic_descriptors_from_files(names):
    
    '''
    list -> dict
    
    returns the semantic descriptors built from the file
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt','alice.txt'])
    >>> d['all']['the']
    >>> 1
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> len(d)
    >>> 30
    
    >>> d = build_semantic_descriptors_from_files(['alice.txt'])
    >>> len(d)
    >>> 45
    
    '''
    words = []
    #open each of the files and get the word breakdown of them
    for file in names:
        fobj = open(file, 'r', encoding = 'utf-8')
        file_content = fobj.read()
        fobj.close()
        #add into the list
        words.extend(get_word_breakdown(file_content))
    return get_all_semantic_descriptors(words)


