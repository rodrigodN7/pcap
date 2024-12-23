#!/usr/bin/env python3

##Working with standard modules
#the dir() function reveal all the names provided through a particular module.
#
import plotly
import math
print(dir())
print(dir(plotly))

for name in dir(math):
    print(name, end="\t")

print(math.sin(math.pi/2))

#In the second method, the import's syntax precisely points out which module's entity (or entities) are acceptable in the code:
from math import e, exp, log, pi, radians, degrees, sin, cos, tan, asin
print(e)
ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
print(pow(e, 1) == exp(log(e)))
print(pow(2,2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


###ceil, floor, trunc
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(y))

#Importing a module
from os import *
message = lambda:system('echo "mesasage"')
message()

#the as keyword
#If you use the import module variant and you don't like a particular module's name (e.g., it's the same as one of your already defined entities, so qualification becomes troublesome) you can give it any name you like - this is called aliasing.

import statistics as estadistica

grades = [10.9,8,7,6,8,9,6,9,8,7,4,5,6,9,8,6,3,6,9,8,7,4,5,7,8,9,6,5,2,3,1,2,3,25,4,7,8,9,8,7,8,9,6,6,9,6,9,8,7,4,18,2,3]
print(grades,'\nThis is the mean: ',round(estadistica.mean(grades),2))
print('This is the median:', round(estadistica.median(grades),2))
print('This is the mode:', round(estadistica.mode(grades),2))

from statistics import mode as moda
print('This is the mode:', round(moda(grades),2))

from statistics import median as mediana, mean as media
print('This is the mediana:', round(mediana(grades),2))
print('This is the moda:', round(media(grades),2))
import os
#dir() function is able to reveal all the names provided through a particular module.
for name in dir(estadistica):
	print(name, end="\t")

#the random() function
#Te algoritm's are not random, they are deterministic and predictable!. Only those physical process those physical processes
#which run completly out of our control (like the intensity of cosmic radiation) may be used as a source of actual random data.
#Data produced by deterministic computers cannot be random in any way.
#A random number generator takes a value called a seed, treats it as an input value, calculates a "random" number based on it
#(the method depends on a chosen algorithm) and produces a new seed value.
#The random factor of the process may be augmented by setting the seed with a number taken from the current time, this may ensure
#that each program launch will start from different seed value(ergo, it will use different random numbers)

#do not confuse random() function with the module random!
#produces a float number x coming from the range (0.0, 1.0), in other words, (0.0 <= x < 1.0)

#generate 8 random numbers.
from random import random
print('\n+++++++')
for i in range(7):
	print(random())
print('+++++++')

#the seed function is able to directly set the generator's seed. We'll show you two of its variants:

   # seed() - sets the seed with the current time;
   # seed(int_value) - sets the seed with the integer value int_value.
#pay attention! due the fact that the seed is always set with the same value (seed(0)), the sequence of generated values always look the same.
from random import random, seed
print('\n+++++++\nseed\n+++++++')
#remeber, seed with a value will deny the random functionality, it means always get same value, no random values
#seed(0)

for i in range(5):
    print(random())
print('+++++++')

"""randrange() and randinit() functions"""

#If you want integer random values, one of the following functions would fit better:

 #   randrange(end)
 #   randrange(beg, end)
 #   randrange(beg, end, step)
 #   randint(left, right)

#The first three invocations will generate an integer taken (pseudorandomly) from the range (respectively):

 #   range(end)
 #   range(beg, end)
 #   range(beg, end, step)

#Note the implicit right-sided exclusion!

#The last function is an equivalent of randrange(left, right+1) - it generates the integer value i, which falls in the range [left, right] (no exclusion on the right side).

#Look at the code in the editor. This sample program will consequently output a line consisting of three zeros and either a zero or one at the fourth place.

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

#The previous functions have one important disadvantage - they may produce repeating values even if the number of subsequent invocations is not greater than the width of the specified range.

#Look at the code below - the program very likely outputs a set of numbers in which some elements are not unique:

for i in range(5):
        print(randrange(1,7), end=',')

#choice() and sample() functions

# choice(sequence)
# sample(sequence, elements_to_choose)

#The first variant chooses a "random" element from the input sequence and returns it.
#The second one builds a list (a sample) consisting of the elements_to_choose element "drawn" from the input sequence.

#In other words, the function chooses some of the input elements, returning a list with the choice. The elements in the sample are placed in random order. Note: the elements_to_choose must not be greater than the length of the input sequence.
print('\n+++++++')
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

#The platform() function
#The platform module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information.
#This is how you can invoke it:
#   platform(aliased = False, terse = False)
#aliased → when set to True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
#terse → when set to True (or any non-zero value) it may convince the function to present a briefer form of the result (if possible)
from platform import platform
print(platform())
print(platform(1))
print(platform(0,1))

#The machine() function
#Sometimes, you may just want to know the generic name of the processor which runs your OS together with Python and your code - a function named machine() will tell you that. As previously, the function returns a string.
from platform import machine
print(machine())

#The processor function
#The processor() function returns a string filled with the real processor name (if possible).
from platform import processor
print(processor())

#The system() function
#A function named system() returns the generic OS name as a string.
from platform import system
print(system())

#The version function
# The OS version is provided as a string by the version() function.
from platform import version
print(version())

#The python_implementation and the python_version_tuple functions
#If you need to know what version of Python is running your code, you can check it using a number of dedicated functions - here are two of them:

#python_implementation() → returns a string denoting the Python implementation (expect CPython here, unless you decide to use any non-canonical Python branch)
#python_version_tuple() → returns a three-element tuple filled with:
#the major part of Python's version;
#the minor part;
#the patch level number.
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
#You can read all about all standard Python modules here:
#https://docs.python.org/3/py-modindex.html


########################
# Modules and packages #
########################

##a module is a kind of container filled with functions - you can pack as many functions as 
#you want into one module and distribute it across the world;
#of course, it's generally a good idea not to mix functions with different application areas 
#within one module (just like in a library - nobody expects scientific works to be put among 
#comic books), so group your functions carefully and name the module containing them in a clear 
#and intuitive way (e.g., don't give the name arcade_games to a module containing functions 
#intended to partition and format hard disks)
#making many modules may cause a little mess - sooner or later you'll want to group your 
#modules exactly in the same way as you've previously grouped functions 
#- is there a more general container than a module?
#yes, there is - it's a package; in the world of modules, a package plays a similar role to a 
#folder/directory in the world of files.
