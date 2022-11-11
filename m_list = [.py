'''
Poem = 'Twinkle, twinkle, little, star, \n      How I wonder what you are! \n       Up above the world so high, \n       Like a diamonnd in the sky. \n Twinkle  twinkle, little star, \n        How I wonder what you are'
print(Poem)

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

print(\n)

import sys
print('python version')
print(sys.version)
print('version info.')
print(sys.version_info)

print(\n)

import datetime
time = datetime.datetime.now()
print('currect date and time: ')
print(time.strftime('%Y-%m-%d \n %H-%M-%S'))

print(\n)

from math import pi

def Area(r):
    r= float(input('radius:))
    area = r * pi
    print(area)
Area(6)

print(\n)

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
#OR
print('\n')

values = input('Input some integer: ')
List = values.split(',')
LIst = list(List)
tuple = tuple(list)
print('list: ',List)
print('tuple: ',tuple)
#OR
print('\n')
values = (input('Using "," to separate integer\nInput some integer : '))
List = values.split(',')
LisT = list(List)
tuple = tuple(List)
print('List: ',LisT)
print('Tuple: ',tuple)

print('\n')

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



#8. Write a Python program to display the first and last colors 
# from the following list. 
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1] )

import os 
 
# Executing a shell command 
# os.system()     
 
# Get the users environment 
# os.environ()    
 
# Returns the current working directory. 
# os.getcwd()    
 
# Return the real group id of the current     process. 
# os.getgid()        
 
# Return the current process’s user id. 
# os.getuid()     
 
# Returns the real process ID of the current process. 
# os.getpid()      
 
# Set the current numeric umask and return the previous umask. 
# os.umask(mask)    
 
# Return information identifying the current operating system. 
# os.uname()      
 
# Change the root directory of the current process to path. 
# os.chroot(path)    
 
# Return a list of the entries in the directory given by path. 
# os.listdir(path)  
 
#Create a directory named path with numeric mode mode. 
# os.mkdir(path)     
 
# Recursive directory creation function. 
# os.makedirs(path)   
 
# Remove (delete) the file path. 
# os.remove(path)     
 
# Remove directories recursively. 
# os.removedirs(path)  
 
# Rename the file or directory src to dst. 
# os.rename(src, dst)   

# Remove (delete) the directory path. 
# os.rmdir(path) 

#The % operator in python for strings is used for 
# something called string substitution.
# String and Unicode objects have one unique 
# built-in operation: the % operator (modulo).

#Usage
#'d' Signed integer decimal.
#'i' Signed integer decimal.
#'o' Signed octal value. (1)
#'u' Obsolete type – it is identical to 'd'. (7)
#'x' Signed hexadecimal (lowercase). (2)
#'X' Signed hexadecimal (uppercase). (2)
#'e' Floating point exponential format (lowercase). (3)
#'E' Floating point exponential format (uppercase). (3)
#'f' Floating point decimal format. (3)
#'F' Floating point decimal format. (3)
#'g' Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. (4)
#'G' Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. (4)
#'c' Single character (accepts integer or single character string).
#'r' String (converts any Python object using repr()). (5)
#'s' String (converts any Python object using str()). (6)
#'%' No argument is converted, results in a '%' character in the result.

#9. Write a Python program to display the examination schedule. 
# (extract the date from exam_st_date). 
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
print( 'The examination will start from : %i / %i / %i'%exam_st_date)
print((exam_st_date))

print('\n')
#OR
exam_st_date =(11, 12, 2014)
print(f'The examination will start from :') 
print(f'\t{exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}')

print('\n')
#OR
exam_st_date = (11,12,2014)
print("The examination will start of exam is: ",end="")
print(exam_st_date[0], exam_st_date[1], exam_st_date[2], sep=" / ")


print('\n')
from datetime import date

print("Enter the first date please: ")
fd = date(int(input("\t\t\tYear: ")), int(input("\t\t\tmonth: ")), int(input("\t\t\tday: ")))
print("Enter the second date please: ")
ld = date(int(input("\t\t\tYear: ")), int(input("\t\t\tmonth: ")), int(input("\t\t\tday: ")))
delta = ld - fd
print("Total diffrences : ",delta.days,"days")

print('\n')

#11. Write a Python program to print the documents 
# (syntax, description etc.) of Python built-in function(s).
#Sample function : abs()
#Expected Result :
#abs(number) -> number
#Return the absolute value of the argument.

print(abs.__doc__)
print('\n')

#12. Write a Python program to print the calendar
#  of a given month and year.
# Note : Use 'calendar' module.

import calendar
year = int(input('enter year: '))
month = int(input('Enter month: '))
print(calendar.month(year,month))

#13. Write a Python program to print the following 'here document'.
#Sample string :
#a string that you "don't" have to escape
#This
#is a ....... multi-line
# heredoc string --------> example

print('''
a string that you 'don't' have to escape
This
is a ....... multi-line
heredoc string --------> example
''')

#exampe
import datetime

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.weekday())
#for weekday monday = 0, sunday = 6
print(tday.isoweekday())
#for isoweekday monday = 1, sunday = 7

print('\n')
tdelta = datetime.timedelta(days=7)
#time delta is the difference between two dates or time.
#here a time delta is create one week ahead.
print(tday + tdelta)
#could be subtracted too to fine old dates
print(tday - tdelta)

bday = datetime.date(2022, 11, 21)

till_bday = bday - tday
print(till_bday.total_seconds())

print(till_bday.total_hours())



#14. Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

'''
