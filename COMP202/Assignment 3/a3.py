def sub_vectors(d1, d2):
    
    '''
    (dict, dict) -> dict
    
    returns the result of substracting the second vector from the first one
    
    >>> d1 = {'a': 3, 'b': 2}
    >>> d2 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> print(d)
    {'a': 1, 'c': -1}
    
    '''
    

    d = {}
    for i in d2:
        if i in d1:
            d[i] = d1[i] - d2[i]
            if d[i] == 0:
                del d[i]
            else:
                d[i] = -d2[i]
                    
    return d
def get_keys(d):
    '''
    dict -> list
    
    returns a list containing all keys in a dictionary in lowercases
    
    >>> d = {'aBc': {'deF': 2, 'Ghi': 4}}
    >>> get_keys(d)
    >>> print(d)
    {'abc', ['def', 'ghi']]
    '''
    keys = []
    sub_keys = []
    for k in d:
        keys.append(k)
        for sub_k in d[k]:
            keys.append(sub_k)
        
        
    for i in keys:
        if i in d:
            lower_key = i.lower()
            d[lower_key] = d.pop(i)
        else:
            for j in d:
                for k in d[j]:
                    if k == i:
                        lower_key = i.lower()
                        sub_dict = d[j]
                        d[lower_key] = sub_dict.pop(k)