#Name: Luyue(Gwen) Guan
#Student ID: 260950108

#Define the global variables
HEARTS = 0
DIAMONDS = 1
CLUBS = 2
SPADES = 3
TWO = 0
THREE = 1
FOUR = 2
FIVE = 3
SIX = 4
SEVEN = 5
EIGHT = 6
NINE = 7
TEN = 8
JACK = 9
QUEEN = 10
KING = 11
ACE = 12

def get_suit(card):
    
    '''
    (int) -> int
    
    Returns the suit of the card
    
    >>> get_suit(7)
    2
    
    >>> get_suit(22)
    1
    
    >>> get_suit(53)
    Please enter a valid number
    
    '''
    
    #All inputs should be positive inputs up to 52
    if 1 <= card <= 52:
        #Get the suit of the card by returning the remainder when card is divided by 4
        if card % 4 == 1:
            return HEARTS
        elif card % 4 == 2:
            return DIAMONDS
        elif card % 4 == 3:
            return CLUBS
        elif card % 4 == 0:
            return SPADES
    else:
        print('Please enter a valid number')
            
            
def get_rank(card):
    
    '''
    (int) -> int
    
    Returns the rank of the card
    
    >>>get_rank(7)
    1
    
    >>>get_rank(50)
    12
    
    >>>get_rank(53)
    Please enter a valid number
    
    '''
    
    if 0 <= card <= 51:
        rank = (card - 1) // 4
        #We use (card-1) because if the number is a multiple of 4
        #it will be returned in the next rank, which will result in an error
        return rank
    else:
        print('Please enter a valid number')


def same_rank(card1, card2):
   
    '''
    (int, int) -> bool
    
    Returns whether the cards are of the same rank
    
    >>>same_rank(1, 3)
    True
    
    >>>same_rank(1, 5)
    False
    
    >>>same_rank(0, 5)
    Please enter a valid number
    
    '''
    
    if 0 <= card1 <= 51 and 0 <= card2 <= 51:
        #Get the rank of each card
        #and return whether they are the same
        return get_rank(card1) == get_rank(card2)
    else:
        print('Please enter a valid number')


def same_suit(card1, card2):
    
    '''
    (int, int) -> bool
    
    Returns whether the cards are of the same suit
    
    >>>same_suit(7, 15)
    True
    
    >>>same_suit(1, 3)
    False
    
    >>>same_suit(0, 5)
    Please enter a valid number
    
    '''
    
    if 1 <= card1 <= 52 and 1 <= card2 <= 52:
        #Get the suit of each card
        #and return whether they are the same
       return get_suit(card1) == get_suit(card2)
    else:
        print('Please enter a valid number')
        
        
def same_color_suit(card1, card2):
    
    '''
    (int, int) -> bool
    
    Returns whether the cards are of the same color suit
    
    >>>same_color_suit(7, 15)
    True
    
    >>>same_color_suit(1, 3)
    False
    
    >>>same_suit(0, 5)
    Please enter a valid number
    
    '''
    
    if 1 <= card1 <= 52 and 1 <= card2 <= 52:
       #Get the suit of each card
        suit_card1 = get_suit(card1)
        suit_card2 = get_suit(card2)

        #The suits 0 and 1 are of the same color
        #and the suits 2 and 3 are of the same color
        #Return whether they are of the same color
        return (suit_card1 <= 1 and suit_card2 <= 1) or (suit_card1 > 1 and suit_card2 > 1)
    else:
        print('Please enter a valid number')        
