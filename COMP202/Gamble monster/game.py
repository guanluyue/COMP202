#Name: Luyue Guan
#Student ID: 260950108

from card2 import *

def calculate_winner(points):
    '''
    list -> list
    
    returns a list containing the indices of the lowest points
    
    >>> calculate_winner([100, 5, 20, 42])
    [1]
    >>> calculate_winner([100, 5, 20, 5])
    [1, 3]
    '''
    
    indices = []
    for i in range(len(points)):
        if points[i] == min(points):
            indices.append(i)
    return indices

def calculate_round_points(hand):
    '''
    list -> int
    
    returns the point value of the given hand
    
    >>> calculate_round_points([1, 2, 3, 4])
    8
    >>> calculate_round_points([49, 50, 51, 52])
    4
    '''
    
    points = 0
    for i in hand:
        if 0 <= get_rank(i) <= 8:
            points += (get_rank(i) + 2)
            continue
        elif 9 <= get_rank(i) <= 11:
            points += 10
            continue
        elif get_rank(i) == 12:
            points += 1
    return points

def is_valid_group(cards):
    '''
    list -> bool
    
    returns if the card forms a set of three or more cards of the same rank
    
    >>> is_valid_group([1, 2, 3])
    True
    >>> is_valid_group([1, 2, 3, 52])
    False
    '''
    if all_same_rank(cards):
        if len(cards) >= 3:
            return True
    return False

def is_valid_sequence(cards):
    '''
    list -> bool
    
    returns if the cards for a valid sequence
    
    >>> is_valid_sequence([1, 5, 9])
    True
    >>> is_valid_sequence([1, 5, 10])
    False
    >>> is_valid_sequence([30, 34])
    False
    >>> is_valid_sequence([34, 38, 30])
    True
    '''
    if all_same_suit(cards):
        #generate a new list containing the rank of all cards
        ranks = []
        for c in cards:
            ranks.append(get_rank(c))
        #put all values in the list in an increasing order
        ranks.sort()
        #chekc if they are in a consecutive order
        min_rank = ranks[0]
        max_rank = ranks[-1]
        if ranks == list(range(min_rank, max_rank + 1)) and len(ranks) >= 3: #this generates a consecutive list starting with the lowest rank
            return True
        else:
            return False
    return False
is_valid_sequence([1, 5, 10])
    