#Name: Luyue Guan
#Student ID: 260950108

from card1 import *
#define global variables
SUITS = [HEARTS, DIAMONDS, CLUBS, SPADES]
RANKS = [TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE]
SUITS_STR = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
RANKS_STR = ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']

def get_card(suit, rank):
    '''
    (int, int) -> int
    
    returns the integer representation of the card with given suit and rank
    
    >>> get_card(HEARTS, TWO)
    1
    >>> get_card(HEARTS, THREE)
    5
    >>> get_card(3, 12)
    52
    '''
    
    #plus one because it's the reverse of (card-1) in card1.py
    return (rank * 4) + suit + 1

def card_to_string(card):
    '''
    int -> str
    
    returns the card's name in the form RANK of SUIT
    
    >>> card_to_string(1)
    'TWO of HEARTS'
    >>> card_to_string(5)
    'THREE of HEARTS'
    >>> card_to_string(52)
    'ACE of SPADES'
    '''
    
    rank = RANKS_STR[RANKS.index(get_rank(card))]
    suit = SUITS_STR[SUITS.index(get_suit(card))]
    return rank + ' of ' + suit

def hand_to_string(hand):
    '''
    list -> str
    
    returns the names of all the cards
    
    >>> hand_to_string([1, 2, 3, 4])
    'TWO of HEARTS, TWO of DIAMONDS, TWO of CLUBS, TWO of SPADES'
    >>> hand_to_string([52])
    'ACE of SPADES'
    '''
    
    names = ''
    for card in hand:
        #return the names string when it's the last element in the list
        if card == hand[-1]:
            names += card_to_string(card)
            return names
        names += card_to_string(card) + ', '
        
def get_deck():
    '''
    none -> list
    
    returns a list of integers containing the 52 cards
    
    >>> deck = get_deck()
    >>>len(deck)
    52
    '''
    
    return list(range(1, 53, 1))

def all_same_suit(cards):
    '''
    list -> bool
    
    returns if all cards in the list are of the same suit
    
    >>> all_same_suit([4, 52])
    True
    >>> all_same_suit([1, 2, 3, 4])
    False
    '''
    
    suit = get_suit(cards[0])
    i = 1
    while i < len(cards):
        if get_suit(cards[i]) != suit:
            return False
        i += 1
    return True

def all_same_rank(cards):
    '''
    list -> bool
    
    returns if all cards in the list are of the same rank
    
    >>> all_same_rank([4, 52])
    False
    >>> all_same_rank([1, 2, 3, 4])
    True
    '''
    
    rank = get_rank(cards[0])
    i = 1
    while i < len(cards):
        if get_rank(cards[i]) != rank:
            return False
        i += 1
    return True
