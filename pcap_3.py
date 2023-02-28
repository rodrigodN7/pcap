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
				input('Press any key to continue!')
			except:
				clear()
				print('Invalid data')
				input('Press enter to continue!')

	clear()
	input('Bye!\n Press enter to finish')
	clear()

			
#if_1()
#minmax()
#spathi()
#my_tax()
#leapcomm()
#while1()
#woddeven()
#countvar()
#secret_num()
#for1()
#for2()
#for3()
#for4()
#my_mississipi()
#break_cont()
knot_km()
