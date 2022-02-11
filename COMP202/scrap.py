#Gwen Guan
#Have you heard the new about the E-maillionaire Lottery?
#You can win big prizes by email.
#By depositing 2 Bitcoin to the lottery's account, a player is emailed with a lottery ticket containing a 10-digit number.
#At the end of the lottery period, a winning number will be drawn and the player whose number matches will be emailed.
#Good luck!

#The lottery is rigged!
#Instead of drawing the winning number at the end of the lottery period
#It is drawn BEFORE any tickets are bought
import random
def draw_winning_number():
    '''

    () -> int
    
    Returns a random 10 digit number
    
    >>>random.seed(1)
    >>>draw_winning_number()
    4280387012
    
    >>>random.seed(2)
    >>>draw_winning_number()
    1242886303
    
    >>>random.seed(3)
    >>>draw_winning_number()
    3337446730
    
    '''
    winning_number = random.randint(1000000000,9999999999)
    #Any random number in this range will have 10 digits
    return winning_number

def buy_ticket(email, winning_number):
    '''
    (str, int) -> str
    
    Return the ticket number corresponding to the email to be sent to the player
    
    >>>random.seed(3)
    buy_ticket('123@gmail.com', 4280387012)
    'Your email is: 123@gmail.com\nYour ticket number: 3337446730'
    
    >>>random.seed(2)
    buy_ticket('lottery@mail.mcgil.ca', 1242886303)
    'Your email is: lottery@mail.mcgil.ca\nYour ticket number: 5659489757'

    >>>random.seed(1)
    buy_ticket('hello@gamil.com', 3337446730)
    'Your email is: hello@gamil.com\nYour ticket number: 4280387012'

    '''
    ticket_number = random.randint(1000000000,9999999999)
    while (ticket_number == winning_number):
        #It will keep generating a new number until it no longer matches the winning number
        ticket_number = random.randint(1000000000,9999999999)
    return 'Your email is: ' + email + '\nYour ticket number: ' + str(ticket_number)
    

print(buy_ticket('123@gmail', draw_winning_number))