#retrieve values of x and y
x = int(input('Enter the first value: '))
y = int(input('Enter the second value: '))
#print whether it is true or false that x is a multiple of y
is_multiple = (x % y) == 0
print('It is', is_multiple, 'that', x, 'is a multiple of', y)

#2
import math