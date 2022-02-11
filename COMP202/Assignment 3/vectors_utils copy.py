#Name: Gwen Guan
#Student ID: 260950108

import math


def add_vectors(v1, v2):
    '''

    (dict, dict) -> NoneType
    
    modifies the first vector by adding the second vector to the first one
    
    >>> v1 = {'a': 1, 'b': 3}
    >>> v2 = {'a': 1, 'c': 1}
    >>> add_vectors(v1, v2)
    >>> print(v1)
    {'a': 2, 'b': 3, 'c': 1}
    >>> print(v2)
    {'a': 1, 'c': 1}
    
    >>> v1 = {'hi': 1}
    >>> v2 = {'hi': 2, 'hello': 2}
    >>> add_vectors(v1, v2)
    >>> print(v1)
    {'hi': 3, 'hello': 2}
    >>> print(v2)
    {'hi': 2, 'hello': 2}

    >>> v1 = {'oof': 2, 'oops': 3}
    >>> v2 = {'oof': 1, 'c': 1}
    >>> add_vectors(v1, v2)
    >>> print(v1)
    {'oof': 3, 'oops': 3, 'c': 1}
    '''
    #first convert into all lowercases
    for i in v2:
        if i in v1:
            v1[i] += v2[i]
        else:
            v1[i] = v2[i]

            
def sub_vectors(d1, d2):
    
    '''
    (dict, dict) -> dict
    
    returns the result of substracting the second vector from the first one
    
    >>> d1 = {'a': 3, 'b': 2}
    >>> d2 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> print(d)
    {'a': 1, 'c': -1}
    
    >>> d1 = {'a': 3, 'b': 2, 'c': 1}
    >>> d2 = {'a': 2, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> print(d)
    {'a': 1, 'c': 1}
    
    >>> d1 = {}
    >>> d2 = {'a': 2, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> print(d)
    {'a': -2, 'b': -2}
    '''
    

    d = {}
    for i in d2:
        if i in d1:
            d[i] = d1[i] - d2[i]
            if d[i] == 0:
                del d[i]
        else:
            d[i] = -d2[i]
    #instances where the vector is not in d2, so we keep them as they are
    for j in d1:
        if j not in d2:
            d[j] = d1[j]
                    
    return d

def merge_dicts_of_vectors(d1, d2):
    
    '''
    (dict, dict) -> NoneType
    
    modifies the first imput by combining it to the second one
    
    >>> d1 = {'s': {'science': 3, 'sugar': 2}, 'b': {'bilibili': 4}}
    >>> d2 = {'b': {'bilibili': 2, 'bluhbluh': 1}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> print(d1['b'])
    {'bilibili': 6, 'bluhbluh': 1}
    
    >>> merge_dicts_of_vectors(d2, d1)
    >>> len(d2)
    2
    >>> d2['s']
    {'science': 3, 'sugar': 2}
    
    >>> d1 = {'a': {'apple': 2}, 'p':{'pear': 1, 'plum': 3}}
    >>> d2 = {'p': {'papaya': 6}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> len(d1)
    2
    >>> len(d1['p'])
    3
    >>> merge_dicts_of_vectors(d2, d1)
    >>> d2['a']['apple']
    2
    >>> d2['p']['papaya']
    12
    
    >>> d1 = {'o': {'oof': 4}, 'l': {'lol': 1, 'lmao': 3}}
    >>> d2 = {'w': {'wyd': 5}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> print(d1)
    {'o': {'oof': 4}, 'l': {'lol': 1, 'lmao': 3}}
    >>> merge_dicts_of_vectors(d2, d1)
    >>> print(d2)
    {'w': {'wyd': 5}}
    '''

    #check if d1 and d2 contain at least one same key
    same_key = 0
    for i in d1:
        if i in d2:
            same_key += 1
    if same_key >= 1:
        for j in d2:
            if j in d1:
                add_vectors(d1[j], d2[j])
            else:
                d1[j] = d2[j]

def get_dot_product(v1, v2):
    
    '''
    (dict, dict) -> int
    returns the dot product of the two vectors
    
    >>> v1 = {'hello': 2, 'hi': 3}
    >>> v2 = {'hello': 3, 'yo': 4, 'hi': 4}
    >>> get_dot_product(v1, v2)
    18
    
    >>> v1 = {'sunday': 3}
    >>> v2 = {'monday': 4, 'tuesday': 3}
    >>> get_dot_product(v1, v2)
    0
    
    >>> v1 = {'what': 1}
    >>> v2 = {'what': 3, 'why': 4}
    >>> get_dot_product(v1, v2)
    3
    '''
    product = 0
    for i in v2:
        if i in v1:
            product += v1[i] * v2[i]
    return product

def get_vector_norm(v):
    
    '''
    dict -> float
    returns the norm of a given vector
    
    >>> v1 = {'hello': 3, 'hi': 4}
    >>> round(get_vector_norm(v1), 2)
    5.0
    
    >>> v2 = {'what': 3}
    >>> get_vector_norm(v2)
    3.0
    
    >>> v3 = {'sunday': 5, 'monday': 6, 'tuesday': 2}
    >>> round(get_vector_norm(v3), 2)
    8.06
    '''
    #first sum up the squares
    sum_of_squares = 0
    for i in v:
        sum_of_squares += v[i] ** 2
    return math.sqrt(sum_of_squares)

def normalize_vector(d):
    '''
    dict -> NoneType
    
    modifies the dictionary by dividing each value by the norm of the vector
    
    >>> v1 = {'hello': 2, 'hi': 4}
    >>> normalize_vector(v1)
    >>> v1
    {'hello': 0.4472135954999579, 'hi': 0.8944271909999159}
    
    >>> v2 = {'what': 3}
    >>> normalize_vector(v2)
    >>> v2
    {'what': 1.0}
    
    >>> v3 = {'sunday': 5, 'monday': 6, 'tuesday': 2}
    >>> normalize_vector(v3)
    >>> v3
    {'sunday': 0.6201736729460423, 'monday': 0.7442084075352507, 'tuesday': 0.24806946917841693}
    '''
    
    #get the norm of the vector
    norm = get_vector_norm(d)
    
    #modify each value dividing by the norm
    for i in d:
        d[i] = d[i] / norm


