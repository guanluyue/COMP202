#Name: Luyue Guan
#Student ID: 260950108
from random import *

def draw(hand, top_discard_card):
    '''
    (list, int) -> str
    
    return randomly 'stock' or 'discard'
    
    >>> import_random_player
    >>> seed(1)
    >>> random_player.draw([4, 50, 15, 21], 5):
    'stock'
    >>> random_player.draw([4, 50, 15, 32], None)
    'stock'
    >>> 
    
    '''
    
    n = randint(0, 1)
    if top_discard_card != None:
        if n == 0:
            return 'stock'
        if n == 1:
            return 'discard'
    else:
        return 'stock'
    
def discard(hand):
    '''
    list -> int
    
    returns a random card in hand
    
    >>> import random_player
    >>> seed(1)
    >>> random_player.discard([4, 50, 15, 21])
    50
    >>> random_player.discard([5, 25, 27, 1, 51])
    27
    >>> random_player.discard([2, 1])
    2
    '''
    #returns a random element in the list
    return hand[randint(0, len(hand)-1)]