'''
Poem = 'Twinkle, twinkle, little, star, \n      How I wonder what you are! \n       Up above the world so high, \n       Like a diamonnd in the sky. \n Twinkle  twinkle, little star, \n        How I wonder what you are'
print(Poem)

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

import sys
print('python version')
print(sys.version)
print('version info.')
print(sys.version_info)

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
import datetime
time = datetime.datetime.now()
print('currect date and time: ')
print(time.strftime('%Y-%m-%d %H-%M-%S'))

from math import pi
def Area(r):
    r= float(input('radius:))
    area = r * pi
    print(area)
Area(6)

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

from math import pi
r = float(input('enter circle radius: '))
Area = pi * (r**2)
print('Area of the circle is: ', Area)

from math import pi
def Area():
    radius = float(input('radius: '))
    area = pi * (radius**2)
    print('AREA = ', area)
Area()

print('\n\t')

import datetime
time = datetime.datetime.now()
print('currect date and time: ')
print(time.strftime('%Y-%m-%d %H-%M-%S'))

#4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi

def Circle_Area():
    Area = pi * (radius**2)
    return Area


radius = float(input('Radius: '))
print(Circle_Area())


#5. Write a Python program which accepts the user's first and last name 
# and print them in reverse order with a space between them.

def UserName():
    FullName = list((firstname, lastname))
    print(list(reversed(FullName)))

firstname = input('Enter first name: ')
lastname = input('Enter last name: ')
print(UserName())

#OR 

fname = input('Enter firstname: ')
lname = input('Enter lastname: ')
print('Your name is: ', lname, fname)


#6. Write a Python program which accepts a sequence of 
# comma-separated numbers from user and generate a list 
# and a tuple with those numbers.
#Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

sample_data = 3,5,7,23
def generate():

    SampleList = list((sample_data))
    SampleTuple = tuple((sample_data))

    print('List: ',SampleList)
    print('Tuple: ',SampleTuple)


generate()


values = input('Input some integer: ')
list = values.split(',')
tuple = tuple(list)
print('list: ',list)
print('tuple: ',tuple)

'''


#7. Write a Python program to accept a filename from the user 
# and print the extension of that.
# Sample filename : abc.java
# Output : java
#You can use the split or the splitext
filename = input('Input the Filename: ')
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

print('\n')

import os
filename = input("Input the Filename: ")

split_tup = os.path.splitext(filename)
#print(split_tup)

Filename = split_tup[0]
File_extenstion = split_tup[1]
File_extenstion = filename.split('.')
print('File Extenstion: ', File_extenstion[1])

print('\n')
#OR

filename = input("Input the Filename: ")

split_tup = os.path.splitext(filename)
File_extenstion = filename.split('.')
print('File Extenstion: ', File_extenstion[1])

import pathlib
