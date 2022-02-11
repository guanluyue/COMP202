#Luyue(Gwen) Guan
#Student ID: 260950108

def calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9):
    
    '''
    (int, int, int, int, int, int, int, int, int) -> str
    
    Calculate and return the checksum with formula given
    
    >>> calculate_isbn_checksum_by_digits(8, 7, 1, 1, 0, 7, 5, 5, 9):
    '7'
    
    >>> calculate_isbn_checksum_by_digits(2, 4, 2, 6, 9, 0, 4, 5, 5)
    '0'
    
    >>> calculate_isbn_checksum_by_digits(8, 7, 6, 6, 5, 3, 4, 1, 3)
    '5'
    
    '''
    
    #Calculate the checksum with the formula given
    checksum = str(( d1 + 2 * d2 + 3 * d3 + 4 * d4 + 5 * d5 + 6 * d6 + 7 * d7 + 8 * d8 + 9 * d9 ) % 11)
    
    #If the checksum is 10, replace it with X
    if checksum == '10':
        return 'X'
    else:
        return checksum

def calculate_isbn_checksum(isbn):
    
    '''
    int -> str
    
    Takes as input the ISBN, calculates and returns the checksum as a string
    
    >>> calculate_isbn_checksum(871107559)
    '7'
    
    >>> calculate_isbn_checksum(385710398)
    '1'
    
    >>> calculate_isbn_checksum(111111111)
    '1'
    
    '''
    
    #Get the number on nth (counting from right to left) digit by dividing by 10^(n-1)
    #For example, d1 = 1234 // ( 10 ** (4 - 1)) = 1
    #Then get the remainder of the number / d1 * 10^(n-1)
    #Repeat the same steps to get the rest of the digits
    d1 = isbn // 100000000
    d2 = (isbn % 100000000) // 10000000
    d3 = (isbn % 10000000) // 1000000
    d4 = (isbn % 1000000) // 100000
    d5 = (isbn % 100000) // 10000
    d6 = (isbn % 10000) // 1000
    d7 = (isbn % 1000) // 100
    d8 = (isbn % 100) // 10
    d9 = isbn % 10
    checksum = str(( d1 + 2 * d2 + 3 * d3 + 4 * d4 + 5 * d5 + 6 * d6 + 7 * d7 + 8 * d8 + 9 * d9 ) % 11)
    return checksum


def is_isbn(isbn, checksum):
    
    '''
    (int, str) -> bool
    
    Check if the checksum of the ISBN is valid
    
    >>> is_isbn(871107559, '4')
    False
    
    >>> is_isbn(111111111, '1')
    True
    
    >>> is_isbn(385710398, '2')
    False

    '''
    
    return calculate_isbn_checksum(isbn) == checksum


def book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
    
    '''
    (int, int, int, int, int, int) -> bool
    
    Check if the book fits in the box
    
    >>> book_fits_in_box(15, 2, 2, 2, 15, 2)
    True
    
    >>> book_fits_in_box(10, 10, 10, 2, 15, 2)
    False
    
    >>> book_fits_in_box(12, 1, 2, 2, 15, 2)
    False
    
    '''
    
    #Check for all possibilities because the book can rotate and flip to fit in the box
    #There are 3 possible ways of pairing up the dimensions of the book with dimensions of the box
    #Return whether the book can fit in the box
    return(book_w <= box_w and book_d <= box_d and book_h <= box_h) or (book_w <= box_h and book_d <= box_w and book_h <= box_d) or (book_w <= box_d and book_d <= box_h and book_h <= box_w)


def get_smallest_box_for_book(book_w, book_d, book_h):
    
    '''
    (int, int, int) -> bool
    
    Check for dimensions of the book and get the smallest size of box
    
    >>> get_smallest_box_for_book(12, 12, 2)
    medium
    
    >>> get_smallest_box_for_book(10, 10, 1)
    small
    
    >>> get_smallest_box_for_book(12, 16, 3)
    large
    
    '''
    
    #Check if the book fits in the small box
    if book_fits_in_box(10, 10, 2, book_w, book_d, book_h):
        return('small')
    #Then check for medium if it does not fit into small
    elif book_fits_in_box(15, 15, 3, book_w, book_d, book_h):
        return('medium')
    #Then check for large if it does not fit into medium
    elif book_fits_in_box(20, 20, 4, book_w, book_d, book_h):
        return('large')
    #Return an empty string if it does not fit into any of the box
    else:
        return ''


def get_num_books_for_box(box_w, box_d, box_h,book_w, book_d, book_h):
    
    '''
    (int, int, int, int, int, int) -> int
    
    Returns the maximum number of identical books that can fit into the box
    
    >>> get_num_books_for_box(10, 5, 5, 5, 5, 2)
    4
    
    >>> get_num_books_for_box(10, 5, 5, 11, 5, 2)
    Sorry, the book does not fit in the box.
    
    >>> get_num_books_for_box(10, 5, 5, 1, 1, 2)
    100
    
    '''
    
    num_book_h = box_h // book_h
    num_book_d = box_d // book_d
    num_book_w = box_w // book_w
    num_book = num_book_h * num_book_w * num_book_d
    if num_book == 0:
        print('Sorry, the book does not fit in the box.')
    else:
        print('The number of equally sized books per box is: ' + str(num_book))
        return num_book
      
        
def main():
    
    '''
    () -> None
    
    Combine all the functions into one system
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice (1-4): 1
    Enter ISBN: 867295849
    Enter checksum: 3
    ISBN is not valid (checksum did not match).
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice (1-4): 2
    Enter book width: 2
    Enter book depth: 3
    Enter book height: 4
    Enter box width: 6
    Enter box depth: 2
    Enter box height: 4
    The book fits in the box.
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice (1-4): 3
    Enter book width: 2
    Enter book depth: 5
    Enter book height: 10
    The book fits into a small box.
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice (1-4): 4
    Enter box width: 10
    Enter box depth: 10
    Enter box height: 4
    Enter book width: 2
    Enter book depth: 4
    Enter book height: 4
    The number of equally sized books per box is: 10
    
    '''
    
    #Welcome the user and display the options
    print('Welcome to the shipment calculation system.')
    print('1) Check ISBN')
    print('2) Check box/book size')
    print('3) Get smallest box size for book')
    print('4) Get num equally-sized books per box')
    #Retrieve user input
    choice = int(input('Enter choice (1-4): '))
    if choice == 1:
        #Check if ISBN is valid
        isbn = int(input('Enter ISBN: '))
        checksum = int(input('Enter checksum: '))
        if is_isbn(isbn, checksum):
            print('ISBN is valid.')
        else:
            print('ISBN is not valid (checksum did not match).')
    elif choice == 2:
        #Check if book fits in the box
        book_w = int(input('Enter book width: '))
        book_d = int(input('Enter book depth: '))
        book_h = int(input('Enter book height: '))
        box_w = int(input('Enter box width: '))
        box_d = int(input('Enter box depth: '))
        box_h = int(input('Enter box height: '))
        if book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
            print('The book fits in the box.')
        else:
            print('Sorry, the book does not fit in the box.')
    elif choice == 3:
        #Get the smallest box size for book
        book_w = int(input('Enter book width: '))
        book_d = int(input('Enter book depth: '))
        book_h = int(input('Enter book height: '))
        smallest_box = get_smallest_box_for_book(book_w, book_d, book_h)
        if smallest_box == '':
            print('Sorry, the book does not fit in the box.')
        else:
            print('The book fits into a ' + smallest_box +' box.')
    elif choice == 4:
        #Get the number of books per box
        box_w = int(input('Enter box width: '))
        box_d = int(input('Enter box depth: '))
        box_h = int(input('Enter box height: '))
        book_w = int(input('Enter book width: '))
        book_d = int(input('Enter book depth: '))
        book_h = int(input('Enter book height: '))
        get_num_books_for_box(box_w, box_d, box_h,book_w, book_d, book_h)
    else:
        print('Please enter a valid choice.')

