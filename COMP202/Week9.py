import random
def trick_or_treat(c1, c2):
    if type(c1) != list:
     print(str(c1))
    elif c1 > c2:
        print(' '.join(c1+c2))
    elif type(c1) == list:
        print(c1[-1])
    elif c1 <= c2:
        print(c1, c2)
    else:
        if random.random() < 0.5:
         print(my_list)
        else:
         raise ZeroDivisionError
            
def print_b(s):
    return s.replace(',', '[') + s.count(',')*']'

my_list = []
for i in range(10):
    my_list.append(i)
my_other_list = my_list + [10]
my_list = my_list[:]
my_third_list = [0, 0]
my_list = my_third_list

def reverse_list(a_list):
    for i in range(1):
        a_list = a_list[::-1]
    return a_list

def remove_dups(nums):
    j = 0 #A1
    while j < len(nums):#G1
        i = 0 #C2
        while i + j < len(nums) -1 and nums[j] == nums[i + j + 1]: #F2
            i += 1 #D3
        nums[j:i + j + 1] = [nums[j]] #E2
        j += 1 #B2
    return nums
            
def scourge_of_existence(my_tuple, my_list):
    t = list(my_tuple)
    for x in my_list:
        t.append(x)
    return t

        
d = {}
d[int('hello')] = 'yes'