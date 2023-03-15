#!/usr/bin/env python3

import os

clear = lambda:os.system('clear')
clear()


"""Parameterized functions"""
#parameters exist only inside functions in which they have been defined
#assigning value to the parameter is done at the time of the function's invocation
#DON'T FORGET!
#parameters live inside functions (this is their natural environment)
#arguments exist outside functions, and are carriers of values passed to corresponding parameters

def message(number):
	print("Enter a number:", number)


message(7)
 
"""Keyword argumenet passing"""
def introduction(first_name, last_name):
	print("Hello, my name is", first_name, last_name)

introduction(first_name = 'James', last_name = 'Bond')
introduction(last_name = 'Skywalker', first_name = 'Luke')

"""mixing positional and keyword arguments"""

def adding(a,b,c):
	print(a, '+', b, '+', c, '=', a + b + c)
adding(1,2,3)
adding(c = 7, b = 2, a = 5)
#adding(2, c = 1, 7) #this generates an error
adding(1, b = 7, c = 8)
#adding(1, 7, b = 8) #this generates an error
adding(1, 7, c = 8)

"""Parametrized function with predefined values"""

def other_intro(first_name, last_name='Noriega'):
	print('Hello, my name is', first_name, last_name)
other_intro('Roko')
other_intro('Roko', 'Sifredi') # this is correct, the second parameter will replace the predefined value

#def add_numbers(a, b=2, c):
#	print(a+b+c)
#add_numbers(a=1,c=3)#this generates an error

"""return instruction"""
#to get functions to return a value (but only for this purpose) you use the return instruction
#NOTE!: return is a python keyword

#return without expression

def new_year(wishes):
	print('Three\nTwo\nOne...')
	if not wishes:
		return
	print('Happy new year')

new_year(True)
new_year(False)

#return with an expression
#it causes the immediate termination of the function's execution (nothing new compared to the first variant)
#moreover, the function will evaluate the expression's value and will return it (hence the name once again) as the function's results.

def boring_function():
	return 777
boring_function() #output anything
x = boring_function() #the returned valu is tored in a variable, so we can see the value
print('The boring_function has returned its result. It\'s:', x)

#None value
#Its data doesn't represent any reasonable value - actually. it's not a value at all; hence, it mustn't take part in any expressions.
#None is a keyword
#print(None  + 2) #this prints an error

value = None
if value is None:
	print('Sorry, you don\'t carry any value')

#NOTE!: Do not forger if a function does not return a certain value using a returm expression clause, it is assumed that it implicitly returns None.

def strange_function(n):
	if(n % 2 == 0):
		return True

x = strange_function(2)
y = strange_function(7)
print(x,y)
print(strange_function(2))
print(strange_function(7))

"""Effects and results: lists and functions"""

#a list can be sent to a function as an argument

def list_sum(my_list):
	s = 0

	for elem in my_list:
		s += elem
	return s

my_list = [1,2,3,4,5,6,7]
res = list_sum(my_list)
print(res)

#or symply
print(list_sum([1,2,3,4,5,6,7]))

def strange_list_fun(n):
	strange_list = []

	for i in range(0,n):
		strange_list.insert(0,i)
	return strange_list
print(strange_list_fun(8))

#leap year, write a function that takes an argument (a year) and returns True if the year is a leap year, or False otherwisei
def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr, '->', end='')
	result = is_year_leap(yr)
	if result == test_results[i]:
		print('ok')
	else:
		print('Failed')
