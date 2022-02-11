def sort_and_find(m, n):
    '''
    (list, int) -> list
    
    find the coordinate of the element n in the matrix m
    
    >>> x = [[0, 22, 32],[3, 26, 37],[7, 26, 37],[15, 35, 39],[34, 39, 45]]
    >>> sort_and_find(x, 15)
    [3,0]
    >>> sort_and_find(x, 18)
    [-1, -1]
    >>> sort_and_find(x, 26)
    [2,1]
    >>> x = [[1],[1,2]]
    >>> sort_and_find(x, 1)
    ValueError
    '''
    
    l = len(m[1])
    for i in m:
        #check if is valid matrix
        if len(i) != l:
            raise ValueError
        #sort the list
        i.sort()
    #implement the algorithm
    r = len(m)-1
    c = 0
    while True:
        e = m[r][c]
        coordinate = [r, c]
        if n == e:
            return coordinate
        elif n < e:
            r -= 1
            if r < 0:
                return [-1, -1]
            continue
        elif n > e:
            c += 1
            if c > l - 1:
                return [-1, -1]
            continue
        

   
        