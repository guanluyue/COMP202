#Name: Luyue Guan
#Student ID: 260950108
from card2 import *
from card1 import *
def draw(hand, top_discard_card):
    '''
    (list, int) -> str
    
    returns the user's choice of discarding or stocking the card
    
    >>> draw([4, 50, 15, 21]), 5)
    Draw location: stock
    >>> print(location)
    stock
    >>> draw([5, 2, 17]), None)
    Draw location: discard
    >>> print(location)
    discard
    '''
    
    if top_discard_card == None:
        return 'stock'
    location = input('Draw location: ')
    return location

def discard(hand):
    '''
    list -> str
    
    returns the card at the user's input index
    
    >>> =discard([4, 50, 15, 21],2)
    0            TWO of SPADES 
    1            ACE of DIAMONDS 
    2            FIVE of CLUBS 
    3            SEVEN of HEARTS 
    Choice: 2
    15
    
    >>> discard([35, 1, 5, 26, 12])
    0            TEN of CLUBS 
    1            TWO of HEARTS 
    2            THREE of HEARTS 
    3            EIGHT of DIAMONDS 
    4            FOUR of SPADES 
    Choice: 3
    26
    
    >>> discard([4, 25, 32, 7, 18, 27])
    0            TWO of SPADES
    1            EIGHT of HEARTS
    2            NINE of SPADES
    3            THREE of CLUBS
    4            SIX of DIAMONDS
    5            EIGHT of CLUBS
    Choice: 0
    4
    '''
    
    for card in range(len(hand)):
        print(card, '          ', card_to_string(hand[card]))
    card_to_discard = hand[int(input('Choice: '))]
    return card_to_discard
