#!/ur/bin/env python3

import os
import time

clear = lambda: os.system('clear')
clear()

print('Equality and inequality')
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)
print("""

***************************************
|Priority Table                       |
***************************************
|Priority	Operator	      |	
|1		+,-		unuary|
|2		**		      |
|3		*,x,/,//,%	      |
|4		+,-		binary|
|5		<,<=,>,>=	      |
|6		==,!=		      |
***************************************

""")

"""IF statement"""

def if_1():

	try:

		num1 = int(input("Enter the firs number: "))
		num2 = int(input("Enter the second number: "))

		if num1 > num2:
			largest = num1
		else:
			largest = num2

		print("The largest number is:", largest)
	except:
		print("Wrong option!")

"""Calculating minimum and maximum of three numbers"""

def minmax():
	
	try:
		num1 = float(input("Enter first number"))
		num2 = float(input("Enter second number"))
		num3 = float(input("Enter third number"))

		largest = max(num1,num2,num3)
		print("The largest is:", largest)
		minimumn = min(num1,num2,num3)
		print("The minimum is:", minimumn)
	except:
		print("Wrong data!")

"""if elif else"""

def spathi():
	
	clear()
	
	name = input("Enter flower name: ")

	if name == "Spathiphyllum":
    		print("Yes - Spathiphyllum is the best plant ever!")
	elif name == "spathiphyllum":
    		print("No, I want a big Spathiphyllum!")
	else:
    		print("Spathiphyllum! Not", name + "!")

"""calculating tax"""

def my_tax():

	clear()

	income = float(input("Enter the annual income: "))
	
	if income < 85528:
		tax = income * 0.18 - 556.02
	else:
		tax = (income - 85528) * 0.32 + 14839.02

	if tax < 0.0:
		tax = 0.0

	tax = round(tax, 0)
	print("The tax is:", tax, "thalers")

"""leap or common"""
def leapcomm():
	
	clear()
	
	year = int(input("Enter a year: "))

	if year < 1582:
		print("Not within the Gregorian calendar period")
	else:
		if year % 4 != 0:
			print("Common year")
		elif year % 100 != 0:
			print("Leap year")
		elif year % 400 != 0:
			print("Common year")
		else:
			print("Leap year")

"""While loop"""

def while1():
	try:
		clear()
		# Store the current largest number here.
		largest_number = -999999999

		# Input the first value.
		number = int(input("Enter a number or type -1 to stop: "))
		
		# If the number is not equal to -1, continue.
		while number != -1:
		# Is number larger than largest_number?
			if number > largest_number:
	        # Yes, update largest_number.
				largest_number = number
	        # Input the next number.
			number = int(input("Enter a number or type -1 to stop: "))

	        # Print the largest number.
			print("The largest number is:", largest_number)
	except:
        	print('invalid')

"""While odd even"""
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
def woddeven():

	try:
		odd_numbers = 0
		even_numbers = 0

		# Read the first number.
		number = int(input("Enter a number or type 0 to stop: "))

		# 0 terminates execution.
		while number != 0:
		    # Check if the number is odd.
			if number % 2 == 1:
			# Increase the odd_numbers counter.
				odd_numbers += 1
			else:
			# Increase the even_numbers counter.
				even_numbers += 1
			# Read the next number.
			number = int(input("Enter a number or type 0 to stop: "))

		# Print results.
		print("Odd numbers count:", odd_numbers)
		print("Even numbers count:", even_numbers)

	except:
		print("Error")

"""Counter controlled loop"""

def countvar():

	try:
		counter = 5
	
		while counter:
			print("Inside the loop", counter)
			counter -= 1
		print("Outside the loop", counter)
	except:
		print("Error")

"""guess the secret number"""

def secret_num():
	secret_number = 777

	print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
	""")
	while True:
		try:
			my_int = int(input('Enter an int: '))  
			while secret_number != my_int:
				try:    
					print('Haha! You\'re stucked in my endless loop')
					my_int = int(input('Enter an int: '))
				except:
					print('That is not a number!')
			print('Correct!')
			break
		except:
			print('That is not a number!')

"""for loop"""

def for1():
	
	for i in range(10):
		print("The value of i is currently", i)

def for2():

	for i in range(2, 8):
		print('Value is:', i)

def for3():

	for i in range(2,8,3):
		print("Value:", i)


def for4():
	
	power = 1
	for expo in range(16):
		print("2 to the power of", expo, "is", power)
		power *= 2

def my_mississipi():

	for i in range (1,6):
		print(i, 'mississipi')
		time.sleep(1)
	print('Ready or not here I come!')

def break_cont():

	print("The break instruction:")
	for i in range(1, 6):
    		if i == 3:
        		break
    		print("Inside the loop.", i)
	print("Outside the loop.")


# continue - example

	print("\nThe continue instruction:")
	for i in range(1, 6):
    		if i == 3:
        		continue
    		print("Inside the loop.", i)
	print("Outside the loop.")

def knot_km():

	while True:
		clear()
		number = input("type quit to exit!\nenter knots to convert: ")
		data = str(number)

		if data == 'quit':
			break
		else:
			try:
				clear()
				data = float(number)
				print(data, 'knots = ',round(data * 1.852, 2), 'kph')
				input('Press enter to continue!')
			except:
				clear()
				print('Invalid data')
				input('Press enter to continue!')

	clear()
	input('Bye!\n Press enter to finish')
	clear()

def vow_eater():
	
	try:
		my_in = str(input('Enter a word:'))
		my_in = my_in.upper()

		for i in my_in:

			if i == 'A':
				continue
			elif i == 'E':
				continue
			elif i == 'I':
				continue
			elif i == 'O':
				continue
			elif i == 'U':
				continue
			else:
				print(i)
	except:
		print('Error')
			
def vow_eater2():

	try:
		word_without_vowels = ""
		my_in = str(input('Enter a word:'))
		my_in = my_in.upper()

		for i in my_in:

			if i == 'A':
				continue
			elif i == 'E':
				continue
			elif i == 'I':
				continue
			elif i == 'O':
				continue
			elif i == 'U':
				continue
			else:
				word_without_vowels += i
		print(word_without_vowels)
    
	except:
		print('Error')

def while_else():

        i = 1
        while i < 5:
                print(i)
                i += 1
        else:
                print("else:", i)

def for_else():

	for i in range(5):
		print(i)
	else:
		print('else', i)

def block_pyr():
	
	blocks = int(input("Enter the number of blocks: "))

	height = 0
	in_layer = 1
	
	while in_layer <= blocks:
		
		height  += 1
		blocks -= in_layer
		in_layer += 1

	print('The height of the pyramid:', height)

def collatz_hyp():
	
	#1. Take any non-negative and non-zero integer number and name it c0.
	#2. If it's even, evaluate a new c0 as c0%2
	#3. Otherwise, if it's odd, evaluate a new c0 as 3 x c0 + 1
	#4. If c0 !=, go back to point 2

	c0 = int(input("Enter c0: "))
	
	if c0 > 1:
		steps = 0
		
		while c0 != 1:
			if c0 % 2 != 0:
				cnew = 3 * c0 + 1
			else:
				cnew = c0 // 2
			print(c0)
			c0 = cnew
			steps += 1
		print("steps =", steps)
	else:
		print("Bad c0 value")


def computer_logic():

	print("""
############
and operator
############

A       B       A and B
0       0          0
1       0          0
0       1          0
1       1          1

############
or opeartor
############

A       B       A or B
0       0          0
1       0          1
0       1          1
1       1          1

############
xor operator
############

A       B       A xor B
0       0          0
1       0          1
0       1          1
1       1          0

############
ot operator
############
A	not A
0	1
1	0

#################
Bitwise operators
#################

&	Ampersand	bitwise conjunction
|	Bar		bitwise disjunction
~	Tilde		bitwise negation
^	Caret		bitwise exclusive or (xor)

& requires exactly two 1s to provide 1 as the result.
| requires at least one 1 to provide 1 as the result.
^ requires exactly one 1 to provide 1 as the result.
Note!: the arguments of these operatorss must be integers; we must not use floats here.
""")

	i = 2
	e = 3
	print(i & e)
	print(i | e)
	print(i ^ e)
	print("""

	i = 00000010
	e = 00000011
	& = 00000010
	| = 00000011
	^ = 00000001  
""")
	print(~0b00000111)
	print('Binary left shift and binary right shift')
	var = 7
	var_right = var >> 1
	var_left = var << 2
	print(bin(var), bin(var_left), bin(var_right))


def lists():
	#indexing lists
	nums_1 = [10,5,7,2,1]
	print(nums_1)
	#assign new value to the first element of the list
	nums_1[0] = 111
	print(nums_1) # prints the whole list
	#value of fifth element to be copied to the second element
	nums_1[1] = nums_1[4]
	print(nums_1)
	#accessing list contents
	print(nums_1[2])
	#len() function takes the list's name as an argument
	#and returns the number of elements currently stored inside the list
	print(len(nums_1))
	#removing elements from a list
	del nums_1[1]
	print(len(nums_1))
	print(nums_1)	
	#NOTE!: you can't access an element which doesn't exist
	#print(nums_1[4])
	#negative indices are legal
	print(nums_1[-3])
	
	#append() and insert() methods
	#list.append(value)
	#list.insert(location, value)
	nums_1.append(9)
	print(nums_1)
	print(len(nums_1))	
	nums_1.insert(0, 17)	
	print(nums_1)
	print(len(nums_1))
	

	numbers = []
	for i in range(17):
		numbers.append(i)
	print(numbers)

	#swap list elements to reverse their order.
	my_list = [10, 1, 8, 3, 5]
	print(my_list)
	my_list[0], my_list[4] = my_list[4], my_list[0]
	my_list[1], my_list[3] = my_list[3], my_list[1]
	print(my_list)
	#using for loop to swap the list
	for i in range(len(my_list) // 2):
		my_list[i], my_list[len(my_list) -i - 1] = my_list[len(my_list) -i - 1], my_list[i]
	print(my_list)

	#lists can beindexed
	my_list = [1, 'a', ["list", 64, [0, 1], False]]
	print(len(my_list))
	print(my_list)

def the_beatles():
	beatles = []
	beatles.append('Jhon Lenon')
	beatles.append('Paul McCartney')
	beatles.append('George Harrison')
	
	for members in range(2):
		beatles.append(input('New band member: '))
	
	print(beatles)
	del beatles[-1]
	del beatles[-1]
	beatles.insert(0, 'Ringo Starr')
	print('The fab:', len(beatles), beatles)


def bubble_sort():

	my_list = [8,10,6,2,4]
	swapped = True

	while swapped:
		swapped = False
		for i in range(len(my_list) - 1):
			if my_list[i] > my_list[i + 1]:
				swapped = True
				my_list[i], my_list[i + 1] = my_list[i + +1], my_list[i]
	print(my_list)


def bubble_sort_interactive():

	my_list = []
	swapped = True
	num = int(input('How many elements do you want to sort'))

	for i in range(num):
		val = float(input('Enter a list element:'))
		my_list.append(val)

	while swapped:
		swapped = False
		for i in range(len(my_list) - 1):
			if my_list[i] > my_list[i + 1]:
				swapped = True
				my_list[i], my_list[i + 1] = my_list[i + +1], my_list[i]
	print('\nSorted:')
	print(my_list)

def sort_reverse_method():
	my_list = [8,10,6,2,4]
	print(my_list)
	my_list.sort()
	print(my_list)
	my_list.reverse()
	print(my_list)

"""Operation on lists"""

def operation_lists():

	list_1 = [1]
	list_2 = list_1
	list_1[0] = 2
	print(list_1,list_2)

	#slices
	#A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list
	#copies the list's contents, not the list's name.
	
	list_1 = [1]
	list_2 = list_1[:]
	list_1[0] = 2
	print(list_1, list_2)
	
	my_list = [10,8,6,4,2]
	new_list = my_list[1:3]
	print(my_list,new_list)		
	my_list = [10,7,4,3,1]
	print(my_list,new_list)
	
	#negative indices
	new_list = my_list[1:-1]
	print(new_list)		
	#if the start specifies an element lying further than the one described by the end (from the list beginning), the slice will be empty:
	new_list = my_list[-1:1]
	print(new_list)		
	my_list = [10,7,4,3,1]
	new_list = my_list[:3]
	print(new_list)		
	new_list = my_list[3:]
	print(new_list)		
	new_list = my_list[1:len(my_list)]
	print(new_list)		
	new_list = my_list[:] #this copies the whole list
	print(new_list)
	#delete slices
	del my_list[1:3]
	print(my_list)		
	del my_list[:]
	print(my_list)
	my_list = [1,2,3]
	del my_list
	#print(my_lismy_listt) # this generates an error
	
def in_not_operators():
	
	my_list = [0, 7, 3, 12, 8]
	print(5 in my_list)
	print(5 not in my_list)
	print(12 in my_list)

def list_greater_value(): 
	#using a list will get greater value from that list
	my_list = [2,17, 11, 3, 5, 1, 9, 7, 15,13]
	largest = my_list[0]

	for i in range(1, len(my_list)):
		if my_list[i] > largest:
			largest = my_list[i]
	print(largest)

def list_greater_value_1():
        #using a list will get greater value from that list
        my_list = [2,17, 11, 3, 5, 1, 9, 7, 15,13]
        largest = my_list[0]

        for i in my_list:
                if i > largest:
                        largest = i
        print(largest)

def list_greater_value_2():
        #using a list will get greater value from that list
        my_list = [2,17, 11, 3, 5, 1, 9, 7, 15,13]
        largest = my_list[0]

        for i in my_list[1:]:
                if i > largest:
                        largest = i
        print(largest)

def find_location_list():
	my_list = [1,2,3,4,5,6,7,8,9,10]
	to_find = 7
	found = False

	for i in range(len(my_list)):
		found = my_list[i] == to_find
		if found:
			break

	if found:
		print('Elements found at index:', i)
	else:
		print('absent')

def remove_repeated():

	my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
	new_list = []
	for number in my_list:  # Browse all numbers from the source list.
		if number not in new_list:  # If the number doesn't appear within the new list...
			new_list.append(number)  # ...append it here.
	my_list = new_list[:]  # Make a copy of new_list.
	print("The list with unique elements only:")
	print(my_list)

	
#if_1()
#minmax()
#spathi()
#my_tax()
#leapcomm()
#while1()
#woddeven()
#countvavow_eater()
#vow_eater2()
#while_else()
#for_else()
#block_pyr()
#collatz_hyp()
#computer_logic()
#lists()
#the_beatles()
#bubble_sort()
#bubble_sort_interactive()
#sort_reverse_method()
#operation_lists()
#in_not_operators()
#list_greater_value()
#list_greater_value_2()
#find_location_list()
remove_repeated()
