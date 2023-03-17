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

"""Functions and scopes"""

#the scope of a function's parameter is the functions itself. The parameter is inaccessible outsid ethe function.
def scope_test():
	xx = 77

scope_test()
#print(xx) #this prints an error as the variable xx is out of scope of the function 
def scope_test1():
	print('Do I kn ow this variable?', my_var1)
my_var1 = 7
scope_test1() #a variable existing outside a function has scope inside the function's body.
print(my_var1)

def scope_test2():
	varx = 2
	print('Var value:', varx)

varx = 7
scope_test2()
print(varx)

"""Functions and scopes: the global keyword"""

def global_func():
	global varz #forces python to refrain from creating a new avriable inside the function
	varz = 	7
	print('DO i know that varz:', varz)

varz = 1
global_func()
print(varz)



"""How the function interacts with its arguments"""
def func_inter(n):
	print('I got', n)
	n += 1
	print('I have:', n)

varp = 7
func_inter(varp)
print(varp)

def factorial_function(m):
	if m < 0:
		return None
	if m < 2:
		return 1
	product = 1

	for i in range(2, m + 1):
		product *= i
	return product

for z in range(10):
	print(z,'! = ', factorial_function(z))

"""fibonacci numbers"""
def fib_nums(v):
	if v < 1:
		return None
	if v < 3:
		return 1

	elem_1 = elem_2 = 1
	the_sum = 0
	
	for i in range (3, v + 1):
		the_sum = elem_1 + elem_2
		elem_1, elem_2 = elem_2, the_sum
	return the_sum

for v in range(1,10):
	print(v, "->", fib_nums(v))

"""Recursion"""
#technique where a function invokes itself

def fib_recursion(b):
	if b < 1:
		return None #terminate recursion
	if b < 3:
		return 1
	return fib_recursion(b - 1) + fib_recursion(b - 2) #recursive call
for g in range(10):
	print(fib_recursion(g))


def countdown(k):
	print(k)
	if k == 0:
		return #terminate recursion
	else:
		countdown(k - 1) #recursive call

countdown(7)

def factorial_recursion(f):
	if f == 1:
		return 1
	else:
		return f * factorial_recursion(f - 1)

print(factorial_recursion(7))
def recursion_error(h):
	return h * recursion_error(h - 1)
#print(recursion_error)# this is an error as function has no termination condition.

"""Sequence types and mutability"""

#A sequence type is a type of data in Python which is able to store more than one value (or less than one, as a sequence may be empty), and these values can be sequentially (hence the name) browsed, element by element.

#As the for loop is a tool especially designed to iterate through sequences, we can express the definition as: a sequence is data which can be scanned by the for loop.

#The second notion − mutability − is a property of any Python data that describes its readiness to be freely changed during program execution. There are two kinds of Python data: mutable and immutable.

#Mutable data can be freely updated at any time − we call such an operation in situ.


"""Tuples"""
# tuples prefer to use parenthesis, whereas lists like to see brackets, although it's also possible to create a tuple just from a set of values separated by commas.

empty_tuple = ()
#print(empty_tuple()) #this generates an error
one_elem_tuple = (1,)
print(one_elem_tuple)
#or
one_elem_tuple1 = 1.,
print(one_elem_tuple1)
my_tup1 = (1,2,4,8)
my_tup2 = 1., .5, .25, .125, 2, 'Alpha', "Beta", True, 0b001001, [17,18,18], (20,21,22)
print(my_tup2)
#get elements from a tuple
print(my_tup2[0])
print(my_tup2[-1])
print(my_tup2[1:])
print(my_tup2[-2:])
print(my_tup2[:])

for elem in my_tup2:
	print(elem)
#you can't modify a tuple's contents! it is not a list!
#my_tup1.append(777) this generate san error
#del my_tup1[0]#this also generates an error
print(my_tup1)

#get len of a tuple
print(len(my_tup1))
#operator + can join tuples together
t1 = my_tup1 + (1000,10000)
print(t1)
#operator * can multiply tuples
t2 = my_tup1 * 3
print(t2)
#in and not in works the same as in list
print(7 in my_tup1)
print(8 in my_tup1)

"""Dictionaries"""
#The dictionary is another Python data structure. It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.
dictionary = {'cat': 'chat', 'dog':'chien', 'horse': 'cheval'}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854312}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#In Python's world, the word you look for is named a key. The word you get from the dictionary is called a value.
#This means that a dictionary is a set of key-value pairs. Note:

 #   each key must be unique − it's not possible to have more than one key of the same value;
 #   a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
 #   a dictionary is not a list − a list contains a set of numbered values, while a dictionary holds pairs of values;
 #   the len() function works for dictionaries, too − it returns the number of key-value elements in the dictionary;
 #   a dictionary is a one-way tool − if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa. 

#NOTE! In Python 3.6x dictionaries have become ordered collections by default. Your results may vary depending on what Python version you're using.

#If you want to get any of the values, you have to deliver a valid key value:
print(dictionary['cat'])
print(phone_numbers['Suzy'])

#you mustn't use a non-existent key. Trying something like this:
#print(phone_numbers['president']) #this generates an error

#search for some french words.

dictionary = {'cat': 'chat', 'dog':'chien', 'horse': 'cheval'}
words = ['cat', 'lion', 'horse']

for word in words:
	if word in dictionary:
		print(word, '->', dictionary[word])
	else:
		print(word, 'is not in the dictionary')

#NOTE! When you write a big or lengthy expression, it may be a good idea to keep it vertically aligned. This is how you can make your code more readable and more programmer-friendly, e.g.:


# Example 1:
my_dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_nums = {'boss': 5551234567,
              'Suzy': 22657854310
}
 
print(my_dictionary)
print(phone_nums)
