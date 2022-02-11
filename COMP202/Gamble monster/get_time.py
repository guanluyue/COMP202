def get_time_str(t):  
    
    hours = str(t // 100 % 12)
    minutes = str((t - t // 100 * 100))

    time_str = hours + ':' + minutes

    

    if t < 1200:

        return time_str + ' am'

    else:

        return time_str + ' pm'

x = 5

s = 'banana'

y = 0

 

def magic(p, q):

    if p < q:

       a = 'apple'

    else:

        p = 'pineapple'

       # *** HERE ***

    return q

 

print(magic(x, y))