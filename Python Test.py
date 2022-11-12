#SIMPLE SIGNING AND LOGIN.
print('Sign-up Here')
Username = input('Please Enter Username: ')
Password = input('Please Enter Password: ')
print('Signing-Up Succesafull')
print('\n')
print('Please Log-In.')
username = input('Please Enter Your Username: ')
password = input('Please Enter Your Password: ')

if Username == username and Password == password:
    print('Log-in Successful.')
else:
    print('Incorrect Details, Please\nPlease Enter Correct Details')
print('LOGING IN....')
print('\n')

#Write a Python program to get the volume of a sphere with radius 6.
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

print('\n', 'OR')

import math
from math import pi
radius = float(input('Enter Radius: '))
print('Find the Volume of a Sphere, using V=3/4*pi*(r**3)')
volume = 4/3 * pi * (radius**3)
print('Volume Of Sphere is', volume)
print('\n', 'OR')

from math import pi

def volumeSphere(Svolume):
    Svolume = 4/3*pi*(radius**3)
    return Svolume

radius = float(input("radius of sphere: "))
print('Volume Of Sphere = ', volumeSphere(radius))
