space = [['Earth', 'Mars'], ['Luna'], ['Ceres', 'Eros', 'Vesta']]
#space[2][2][2:]+space[0][1][2:]

def r(m, old, new):
    '''
    a = [[1,4,5,4],[5,4,0],[-1,2,4]]
    r(a, 4, 100)
    3
    '''
    c = 0
    for j in m:
        for i in range(len(j)):
            if j[i] == old:
                j[i] = new
                c += 1
                break
    return c
                
            
a = [[1,4,5,4],[5,4,0],[-1,2,4]]
#D1 H1 B2 J3 C4 G4 A4 K1

my_list = [[1,2],[1,2,3]]
def d(my_list):
    c = []
    for a in my_list:
        for b in a:
            c += [[b]]
    return c

def s(x,y):
    if len(y) != len(x):
        raise ValueError()
    z = []
    for i in range(len(x)):
        if y[i]<-len(x[i]) or y[i]>=len(x[i]):
            raise ValueError()
        z.append(x[i][y[i]])
    return z

print(s([[8,4,5],[2],[9,5,3,1]],[-1,0,4]))


