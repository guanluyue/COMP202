# Author: Gwen Guan
# This is a program to greet everyone.

print ("Hello World!")

#Escape sequences are sequences of characters that represents a pecial character.
#\n represents the character 'new line'
#\" or \' represent quotation marks
#\t represents a tab
print('\"Help! I need sombody.\" \n\"Help! Not just anybody.\"')

#A value is a basic thing that can be manipulated by a program, like a letter or a number.
#Examples of calues are: 5(integer),2.3(float), 'hello'(string).
#Type-casting: int(x):converts the calue x into a value of type int
print(int(5.00))

#initializing a variable
my_fav_number = 7
print ('my fav number is', my_fav_number)

temp_F = 85
temp_C = round((temp_F - 32) * (5 / 9)) 

print(str(temp_F) + ' F is equivalent to ' + str(round((temp_F - 32) * (5 / 9))) + ' Celcius')
print(str(temp_F) + ' F is equivalent to ' + str(temp_C) + ' Celcius')
message = str(temp_F) + ' F is equivalent to ' + str(temp_C) + ' Celcius'
print (message)

help('keywords')

# Program that retrieves a mesage from the use
# and displays it back to the screen
print('Do you have anything to say?')
user_message = input()
print ('You just said: ' + user_message +'.')

user_message = input('Do you have anything to say?\n')
print ('You just said: ' + user_message +'.')

# Simple Calculator
integer1 = input('the first integer is:\n')
integer2 = input('the second integer is:\n')
print('the result of', integer1, '+', integer2 , 'is:', int(integer1) + int(integer2))