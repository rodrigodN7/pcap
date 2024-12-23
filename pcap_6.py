#!/usr/bin/env python3

#strings, a brief vies
#First of all, Python's strings (or simply strings, as we're not going to discuss any other language's strings) are immutable sequences.

word = 'by'
print(word)
print(len(word))
empty = ''
print(len(empty))
i_am = 'I\'m'
print(i_am)
print(len(i_am))

#print a multiline
multiline = '''Line #1
Line #2'''

print(multiline)
print(len(multiline))

#operations on strings
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#the ord() function
#If you want to know a specific character's ASCII/UNICODE code point value, you can use a function named ord() (as in ordinal).
#The function needs a one-character string as its argument – breaching this requirement causes a TypeError exception, and returns a number representing the argument's code point.

char_1 = 'a'
char_2 = 'α'
char_3 = ' '  # space
char_4 = 'ę'

print(ord(char_1))
print(ord(char_2))
print(ord(char_3))
print(ord(char_4))

#The chr() function
#If you know the code point (number) and want to get the corresponding character, you can use a function named chr().
#The function takes a code point and returns its character.
#Invoking it with an invalid argument (e.g., a negative or invalid code point) causes ValueError or TypeError exceptions.

print(chr(97))
print(chr(945))

#strings as sequences
#Strings aren't lists, but you can treat them like lists in many particular cases.
#For example, if you want to access any of a string's characters, you can do it using indexing, just like in the example below. Run the program:
the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

#iterating through the string

for character in the_string:
    print(character, end=' ')

print()

#slices
alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#The in operator
#The in operator shouldn't surprise you when applied to strings – it simply checks if its left argument (a string) can be found anywhere within the right argument (another string).
#The result of the check is simply True or False.

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

#not in operator.
print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

#Python strings are immutable
#We've also told you that Python's strings are immutable. This is a very important feature. What does it mean?

#This primarily means that the similarity of strings and lists is limited. Not everything you can do with a list may be done with a string.

#The first important difference doesn't allow you to use the del instruction to remove anything from a string.
#this do not work!
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#del alphabet[0]

#The only thing you can do with del and a string is to remove the string as a whole. Try to do it.
#Python strings don't have the append() method – you cannot expand them in any way.
#this do not work
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet.append("A")

#with the absence of the append() method, the insert() method is illegal, too:
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet.insert(0, "A")

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

#min() function
#The function finds the minimum element of the sequence passed as an argument. There is one condition – the sequence (string, list, it doesn't matter) cannot be empty, or else you'll get a ValueError exception.
print(min("aAbByYzZ"))

# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

#max()
#Similarly, a function named max() finds the maximum element of the sequence.
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

#the index() method
#The index() method (it's a method, not a function) searches the sequence from the beginning, in order to find the first element of the value specified in its argument.

#Note: the element searched for must occur in the sequence – its absence will cause a ValueError exception.

#The method returns the index of the first occurrence of the argument (which means that the lowest possible result is 0, while the highest is the length of the argument decremented by 1).
# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#The list() function
#The list() function takes its argument (a string) and creates a new list containing all the string's characters, one per list element.

#Note: it's not strictly a string function - list() is able to create a new list from many other entities (e.g., from tuples and dictionaries).

#Take a look at the code example in the editor.
# Demonstrating the list() function:
print(list("abcabc"))

#The count() method
#The count() method counts all occurrences of the element inside the sequence. The absence of such elements doesn't cause any problems.
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

#The capitalize method
#The capitalize() method does exactly what it says – it creates a new string filled with characters taken from the source string, but it tries to modify them in the following way:

#    if the first character inside the string is a letter (note: the first character is an element with an index equal to 0, not just the first visible character), it will be converted to upper-case;
#    all remaining letters from the string will be converted to lower-case.

#Don't forget that:

#    the original string from which the method is invoked is not changed in any way – a string's immutability must be obeyed without reservation;
#    the modified string (in this case, capitalized) is returned as a result – if you don't use it in any way (assign it to a variable, or pass it to a function/method) it will disappear without a trace.

#Note: methods don't have to be invoked from within variables only. They can be invoked directly from within string literals. We're going to use that convention regularly – it will simplify the examples, as the most important aspects will not disappear among unnecessary assignments.
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

#The center method
#The centering is actually done by adding some spaces before and after the string.

#Don't expect this method to demonstrate any sophisticated skills. It's rather simple.
print('[' + 'alpha'.center(10) + ']')

#If the target field's length is too small to fit the string, the original string is returned.
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

#The two-parameter variant of center() makes use of the character from the second argument, instead of a space. Analyze the example below:
print('[' + 'gamma'.center(20, '*') + ']')

#The endswidth() method
#The endswith() method checks if the given string ends with the specified argument and returns True or False, depending on the check result.

#Note: the substring must adhere to the string's last character – it cannot just be located somewhere near the end of the string.
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

#The find method
#The find() method is similar to index(), which you already know – it looks for a substring and returns the index of the first occurrence of this substring, but:

#    it's safer – it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
#    it works with strings only – don't try to apply it to any other sequence.

print("Eta".find("ta"))
print("Eta".find("mma"))
#Note: don't use find() if you only want to check if a single character occurs within a string - the in operator will be significantly faster.
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha')
