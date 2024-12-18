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
from random import random
for i in range(5):
	print(random())

#the seed function is able to directly set the generator's seed. We'll show you two of its variants:

   # seed() - sets the seed with the current time;
   # seed(int_value) - sets the seed with the integer value int_value.

from random import random, seed

seed(0)

for i in range(5):
    print(random())

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

for i in range(5):
        print(randrange(1,7), end=' ')
