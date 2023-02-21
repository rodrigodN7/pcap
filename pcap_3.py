#!/ur/bin/env python3

import os

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

if_1()
minmax()
spathi()
my_tax()
leapcomm()
