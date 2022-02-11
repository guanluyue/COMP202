#Name: Gwen Guan
#Student ID: 260950108
from vectors_utils import *
import math

def get_semantic_descriptor(w, s):
    
    '''
    (string, list) -> dict
    
    returns a dictionary representing the semantic descriptor vector of the word
    w computed from the sentence s
    
    >>> s = ['how', 'are', 'you', 'doing']
    >>> w = 'how'
    >>> get_semantic_descriptor(w, s)
    {'are': 1, 'you': 1, 'doing': 1}
    
    >>> s = ['bee','bap','bee','bap','boo']
    >>> w = 'bap'
    >>> get_semantic_descriptor(w, s)
    {'bee': 2, 'boo': 1}
    
    >>> s = ['how', 'are', 'you', 'doing']
    >>> w = 'good'
    >>> get_semantic_descriptor(w, s)
    {}
    
    '''
    
    d = {}
    if w not in s:
        return {}
    for i in s:
        if i == w:
            continue
        else:
            d[i] = s.count(i)
    return d

def get_all_semantic_descriptors(s):
    
    '''
    list -> dict
    
    returns a dictionary that contains all the semantic descriptor vectors
    in the given nested list
    
    >>> s = [['a', 'b', 'c'], ['b', 'c']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['b']
    {'a': 1, 'c': 2}
    
    >>> s = [['it', 'is', 'almost', 'christmas'], ['and', 'final', 'season']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['christmas']
    {'it': 1, 'is': 1, 'almost': 1}
    
    >>> get_all_semantic_descriptors([['hello'],['goodbye']])
    {'hello': {}, 'goodbye': {}}
    
    '''
    
    d = {}
    for sentence in s:
        #get the semantic descriptor of each word in a sentence
        for word in sentence:
            sub_d = {}
            #check if the word is already a key in the dictionary
            if word not in d:
                d[word] = get_semantic_descriptor(word, sentence)
            #if it is, then merge the two dictionaries
            else:
                sub_d[word] = get_semantic_descriptor(word, sentence)
                merge_dicts_of_vectors(d, sub_d)
    return d

def get_cos_sim(v1, v2):
    
    '''
    (dict, dict) -> float
    
    returns the cosine similarity between the two dictionaries given
    
    >>> round(get_cos_sim({'apple': 3, 'pear': 2, 'orange': 5}, {'pineapple': 4}), 2)
    0.0
    >>> round(get_cos_sim({'apple': 3, 'pear': 2, 'orange': 5}, {'apple': 3, 'pear': 2, 'orange': 5}), 2)
    1.0
    >>> round(get_cos_sim({'apple': 3, 'pear': 2}, {'apple': 3, 'pear': 1}), 2)
    0.96
    >>> round(get_cos_sim({'apple': 3, 'pear': 2, 'orange': 5}, {}), 2)
    Traceback (most recent call last):
    ZeroDivisionError
    
    '''
    
    #calculate the dot product and vector norms seperately using helper functions
    dot_product = get_dot_product(v1, v2)
    v1_norm = get_vector_norm(v1)
    v2_norm = get_vector_norm(v2)
    #raise ZeroDivisionError is one of the norms is 0
    if v1_norm == 0 or v2_norm == 0:
        raise ZeroDivisionError
    return dot_product / (v1_norm * v2_norm)

def get_euc_sim(v1, v2):
    
    '''
    (dict, dict) -> float
    
    returns the similarity between the two using the negative euclidean distance
    
    >>> get_euc_sim({'a': 3, 'b': 4}, {'a': 3, 'b': 4})
    0.0
    >>> get_euc_sim({'a': 1, 'b': 4}, {'a': 6, 'b': 4})
    -5.0
    >>> round(get_euc_sim({'a': 1, 'b': 4}, {'c': 6, 'd': 4}), 2)
    -8.31
    
    '''
    
    #get the difference of the two dicts
    sub = sub_vectors(v1, v2)
    #get the norm of both vectors
    norm = get_vector_norm(sub)
    euc_sim = 0 - norm
    return euc_sim

def get_norm_euc_sim(v1,v2):
    
    '''
    (dict, dict) -> float
    
    returns the similarity between the two using the negative euclidean distance between the normalized vectors
    
    >>> get_norm_euc_sim({'a': 3, 'b': 4}, {'a': 3, 'b': 4})
    -0.0
    >>> round(get_norm_euc_sim({'a': 1, 'b': 4}, {'a': 6, 'b': 4}), 2)
    -0.72
    >>> round(get_norm_euc_sim({'a': 1, 'b': 4}, {'c': 6, 'd': 4}), 2)
    -1.41
    
    '''
    #normalize the two vectors
    normalize_vector(v1)
    normalize_vector(v2)
    #get the difference of the two
    sub = sub_vectors(v1, v2)
    return -get_vector_norm(sub)

