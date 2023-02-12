#!/usr/bin/env python3

print("""

What makes language?
alphabet: set of symbols used to build words of certain languages
lexis: aka a dictionary; a set of words the language offers its users
syntax: a set of rules used to determine if a certain string of words form a valid sentence
semantics: a set of rules determining if a certain phrase makes sense.
IL: Instruction list is in fact the alphabet of a machine language.

""")

print('Hello from python')
print("""

	These are triple quotes!

""")
print('Sum is:', 7 + 10)
print('this is \\n \nthis is the effect of \\n')

#end keyword
print("My name is", "Python.", end=" ")
print("Monty Python", end = "!!!!!!\n")

#sep keyword
print("My", "Name", "is", "Rodrigo", sep="-")

#literals and variables
#function type let us know the type of data
print(type("2")) #this is a string
print(type(2)) #this is an integer
print(type(7.1))
print(0o123)
print(type(0o123))
print(0xff)
print(type(0x15))
print(0b101)
print(type(0b101))
print(7E8)
print(0.000000000000000000000000007)
print(7E-12)

#NOTE: Python 3.6 has introduced underscores in numeric literals, allowing for
#placing single underscores between digits and after base specifiers for improved readability.
#This feature is not available in older versions of Python.
print(111_111_111)
print(-111_111_111)
print(+111_111_111)

#coding strings
print('\'First\' string')
print("'Second ' string")
print('"Third" string')
print("\"Fourth\" string")

#boolean values
print(True > False)
print(True < False)

#Basic operators, python as a calculator
#+ , -, *, /, //, %, **
print("\nExponentiation. pow")
print(pow(2,3))
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print("\nMultiplication")
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print("\nDivision\nThe result produced by the division operator is always a float")
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print("\nInteger division, also called floor division\nIts result lacks the fractional part - it's absent (for integers),\nor is always equal to zero (for floats); this means that the results are always rounded\nIt confirms to the integers vs float rule ")
print( 6 // 3)
print( 6 // 3.)
print( 6. // 3)
print( 6. // 3.)
print( 6 // 4) #this prints only the int result
print("\nReminder or modulo")
print(12%5)
print("\nAddition and substratcion")
print(7 + 5)
print(7 + 5.)
print(7. + 5)
print(7. - 5.)
print(7. - 5.)
print(7. - 5.)
print(7. - 5.)
print(5 - 7)
print(5 - 7.)
print(5. - 7)
print(5. - 7.)
print("""
Operator precedence
**
+,-	unuary	note:unary operators located next to the right of the power operator bind more strongly
*, /, //, %
+,-	binary
""")
print(2 * 3 % 5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print("The exponentiation operator uses right-sided binding")
print(2 ** 3 ** 2)
print("Subexpressions in parentheses are always calculated first")
print(15 - 1 * (5 * (1 + 2)))
print("""

	Variables:

    the name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
    the name of the variable must begin with a letter;
    the underscore character is a letter;
    upper- and lower-case letters are treated as different (a little differently than in the real world - Alice and ALICE 
    are the same first names, but in Python they are two different variable names, and consequently, two different variables);
    the name of the variable must not be any of Python's reserved words (the keywords - we'll explain more about this soon).


""")
