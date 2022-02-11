#Name: Luyue(Gwen) Guan
#Student ID: 260950108


#Define each of the four smoothie types, sizes, and toppings as global variables
SMOOTHIE1_NAME = 'Pineapple Banana'
SMOOTHIE1_COST = 4.99
SMOOTHIE2_NAME = 'Almond Basil'
SMOOTHIE2_COST = 6.49
SMOOTHIE3_NAME = 'Purple Surprise'
SMOOTHIE3_COST = 0.99
SMOOTHIE4_NAME = 'Onion Toffee'
SMOOTHIE4_COST = 9.99
TOPPING1_NAME = 'no topping'
TOPPING2_NAME = 'cinnamon'
TOPPING3_NAME = 'chocolate shavings'
TOPPING4_NAME = 'shredded coconut'
TOPPING1_COST = 0.0
TOPPING2_COST = 1.0
TOPPING3_COST = 1.0
TOPPING4_COST = 1.0
SIZE1_NAME = 'small'
SIZE1_COST = -2.0
SIZE2_NAME = 'medium'
SIZE2_COST = 0.0
SIZE3_NAME = 'large'
SIZE3_COST = 2.0
SIZE4_NAME = 'galactic'
SIZE4_COST = 100.0


def pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4):
    
    '''
    (str, str, float, str, float, str, float, str, float) -> str

    Displays the options and return customer's choice
    
    >>> pose_question_with_costs('What smoothie would you like?', SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST, SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    Pineapple Banana
    
    >>> pose_question_with_costs('What smoothie would you like?', SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST, SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    Almond Basil
    
    >>> pose_question_with_costs('What smoothie would you like?', SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST, SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    Onion Toffee
    
    '''
    
    #Display the question and options for the customer
    print(question)
    print('1)       $ ' + str(cost1) + '          ' + option1)
    print('2)       $ ' + str(cost2) + '          ' + option2)
    print('3)       $ ' + str(cost3) + '          ' + option3)
    print('4)       $ ' + str(cost4) + '          ' + option4)
    
    #Retrieve customer's choice
    choice = input('Your choice (1-4):')
    
    #Return option1-4 as a str according to customer's choice
    if choice == '1':
        print('You have selected ' + option1)
        return option1
    
    elif choice == '2':
        print('You have selected ' + option2)
        return option2
    
    elif choice == '3':
        print('You have selected ' + option3)
        return option3
    
    elif choice == '4':
        print('You have selected ' + option4)
        return option4
    
    #Return an empty string for an invalid input
    else:
        print('Sorry, that is not a valid option.')
        return ''

def calculate_subtotal(smoothie_type, smoothie_size, topping):
    
    '''
    (str, str, str) -> float
    
    Sum of smoothie, size, and topping into a floating number

    >>> calculate_subtotal('Almond Basil', 'small', 'no topping')
    4.49
    
    >>> calculate_subtotal('Pineapple Banana', 'galactic', 'shredded coconut')
    105.99
    
    >>> calculate_subtotal('Purple Surprise', 'medium', 'cinnamon')
    1.99
    '''
    
    #Convert type of smoothie to cost in floats
    if smoothie_type == SMOOTHIE1_NAME:
        smoothie_cost = SMOOTHIE1_COST
    
    elif smoothie_type == SMOOTHIE2_NAME:
        smoothie_cost = SMOOTHIE2_COST
    
    elif smoothie_type == SMOOTHIE3_NAME:
        smoothie_cost = SMOOTHIE3_COST
    
    elif smoothie_type == SMOOTHIE4_NAME:
        smoothie_cost = SMOOTHIE4_COST
    
    #Convert size of smoothie to cost in floats
    if smoothie_size == SIZE1_NAME:
        size_cost = SIZE1_COST
    
    elif smoothie_size == SIZE2_NAME:
        size_cost = SIZE2_COST
    
    elif smoothie_size == SIZE3_NAME:
        size_cost = SIZE3_COST
    
    elif smoothie_size == SIZE4_NAME:
        size_cost = SIZE4_COST
    
    #Convert cost of tooping to cost in floats
    if topping == TOPPING1_NAME:
        topping_cost = TOPPING1_COST
    
    #Use TOPPING2_COST for the costs for other toppings because they have the same price
    else:
        topping_cost = TOPPING2_COST
    
    #Calculate the subtotal in float by adding up the variables above and return it
    subtotal = round(smoothie_cost + size_cost + topping_cost, 2)
    return subtotal

def print_receipt(subtotal, smoothie_type, smoothie_size, topping):
    
    '''
    (float, str, str, str) -> str
        
    Print the receipt with their order, subtotal, taxes and total
    
    >>> print_receipt(4.99, 'Almond Basil', 'small', 'no topping')
        You ordered a small Almond Basil smoothie
        Smoothie cost: $4.99
        GST:    $0.25
        QST:    $0.5
        Total:  $5.74
        
    >>> print_receipt(105.99, 'Pineapple Banana', 'galactic', 'chocolate shavings')
        You ordered a galactic Pineapple Banana smoothie with chocolate shavings
        Smoothie cost: $105.99
        GST:    $5.3
        QST:    $10.57
        Total:  $121.86
        
    >>> print_receipt(1.99, 'Purple Surprise', 'medium', 'cinnamon')
        You ordered a medium Purple Surprise smoothie with cinnamon
        Smoothie cost: $1.99
        GST:    $0.1
        QST:    $0.2
        Total:  $2.29
        
    '''
    
    #Display customer's order with smoothie type, size and topping as a receipt
    if topping == 'no topping':
        print('You ordered a ' + smoothie_size + ' ' + smoothie_type + ' smoothie')
    else:
        print('You ordered a ' + smoothie_size + ' ' + smoothie_type + ' smoothie with ' + topping)
    #Display the cost of smoothie with taxes rounded to 2 decimal places
    qst = round(float(0.09975 * subtotal), 2)
    gst = round(float(0.05 * subtotal), 2)
    total = round(subtotal + gst + qst, 2)
    print('Smoothie cost: $' + str(subtotal))
    print('GST:    $' + str(gst))
    print('QST:    $' + str(qst))
    print('Total:  $' + str(total))
    return total


def order():
    
    '''
    () -> str
    
    Welcomes the user to the order system and execute other functions

    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    What smoothie would you like?
    1)       $ 4.99          Pineapple Banana
    2)       $ 6.49          Almond Basil
    3)       $ 0.99          Purple Surprise
    4)       $ 9.99          Onion Toffee
    Your choice (1-4):1
    You have selected Pineapple Banana
    Unfortunately, we are out of Pineapple Banana
    You will be served on Onion Toffee
    What size would you like?
    1)       $ -2.0          small
    2)       $ 0.0          medium
    3)       $ 2.0          large
    4)       $ 100.0          galactic
    Your choice (1-4):2
    You have selected medium
    What topping would you like?
    1)       $ 0.0          no topping
    2)       $ 1.0          cinnamon
    3)       $ 1.0          chocolate shavings
    4)       $ 1.0          shredded coconut
    Your choice (1-4):1
    You have selected no topping
    You ordered a medium Onion Toffee smoothie
    Smoothie cost: $9.99
    GST:    $0.5
    QST:    $1.0
    Total:  $11.49
    
    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    What smoothie would you like?
    1)       $ 4.99          Pineapple Banana
    2)       $ 6.49          Almond Basil
    3)       $ 0.99          Purple Surprise
    4)       $ 9.99          Onion Toffee
    Your choice (1-4):3
    You have selected Purple Surprise
    Unfortunately, we are out of Purple Surprise
    You will be served on Onion Toffee
    What size would you like?
    1)       $ -2.0          small
    2)       $ 0.0          medium
    3)       $ 2.0          large
    4)       $ 100.0          galactic
    Your choice (1-4):1
    You have selected small
    What topping would you like?
    1)       $ 0.0          no topping
    2)       $ 1.0          cinnamon
    3)       $ 1.0          chocolate shavings
    4)       $ 1.0          shredded coconut
    Your choice (1-4):1
    You have selected no topping
    You ordered a small Onion Toffee smoothie
    Smoothie cost: $7.99
    GST:    $0.4
    QST:    $0.8
    Total:  $9.19
    
    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    What smoothie would you like?
    1)       $ 4.99          Pineapple Banana
    2)       $ 6.49          Almond Basil
    3)       $ 0.99          Purple Surprise
    4)       $ 9.99          Onion Toffee
    Your choice (1-4):three
    Sorry, that is not a valid option.
    
    '''

    #Welcome the customers to Smooth Smoothies smoothie system for ordering smoothies
    print('Welcome to Smooth Smoothies Smoothie Ordering System\nHave you tried our new Onion Toffee smoothie?')

    smoothie_type = pose_question_with_costs('What smoothie would you like?', SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST, SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    #Display the smoothie menu, retrieve customer's choice and store as a variable
    #Display customer's choice and inform that they will be served on Onion Toffee if they selected anything else
    if smoothie_type == '':
        return
    elif smoothie_type != 'Onion Toffee':
        print('Unfortunately, we are out of ' + smoothie_type)
        smoothie_type = 'Onion Toffee'
        print('You will be served on ' + smoothie_type)
    

    #Display options for sizes, retrieve customer's choice, and store as a variable
    smoothie_size = pose_question_with_costs('What size would you like?', SIZE1_NAME, SIZE1_COST, SIZE2_NAME, SIZE2_COST, SIZE3_NAME, SIZE3_COST, SIZE4_NAME, SIZE4_COST)
    
    
    #Display options for toppings, retrieve customer's choice, and store as a variable
    topping = pose_question_with_costs('What topping would you like?', TOPPING1_NAME, TOPPING1_COST, TOPPING2_NAME, TOPPING2_COST, TOPPING3_NAME, TOPPING3_COST, TOPPING4_NAME, TOPPING4_COST)
    
    #Store the result of the subtotal calculation as a variable
    subtotal = calculate_subtotal(smoothie_type, smoothie_size, topping)
    print_receipt(subtotal, smoothie_type, smoothie_size, topping)

