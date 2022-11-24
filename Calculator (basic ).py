#Calculator(BASIC)
#1st def the func., add su b mul, div
#print options to the user
#ask for values
#call the func
#while loop  to countinue the program til user quita


def add(a, b):
    answer = a+b
    print(str(a) + '+' + str(b) + '=' + str(answer))
    #print(f'{a}' + '{b}' '=' '{answer}')

def sub(a, b):
    answer= a-b
    print(str(a) + '-' + str(b) + '=' + str(amswer))

def mul(a, b):
    answer= a*b
    print(str(a) + '*' + str(b) + '=' + str(amswer))

def div(a, b):
    answer= a/b
    print(str(a) + '/' + str(b) + '/' + str(amswer))
while True:    #to keep the opration in loop til the quit botton is used.
    print(A. Addition)
    print(A. Subtraction)
    print(C. multiplication)
    print(A. Division)
    print(A. Exit)

    choice = input('input you choice: ')

    if choice == 'a' or choice == 'A':
        print('Addition')
        a=int(input('Input First Number: '))
        b=int(input('Input Second Number: '))
        add(a, b)
    elif choice == 'b' or choice == 'B':
        print('Subtration')
        a=int(input('Input First Number: '))
        b=int(input('Input Second Number: '))
        sub(a, b)
    elif choice == 'c' or choice == 'C':
        print('Division')
        a=int(input('Input First Number: '))
        b=int(input('Input Second Number: '))
        div(a, b)
    elif choice == 'd' or choice == 'D':
        print('Multiplication')
        a=int(input('Input First Number: '))
        b=int(input('Input Second Number: '))
        mul(a, b)
    elif choice == 'e' or choice == 'E':
        print('Progrom don finish')
        quit()
        
        
        
        
        
        
#TRY this with tkinter.

import tkinter
from tkinter import *

root=Tk()
root.title('simple Calculator')
root.geometry('500x600+100+200')
root.resizable(0,0)
root.configure(bg='#17161b')

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation= ""
    label_result.config(text=equation)

def calculate():
    global equation
    result= ""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result= "error"
            equation= ""
    label_result.config(text=result)

label_result=Label(root, width=25,height=2, text='',font=('arial',30))
label_result.pack()

Button(root, text='c', width=5, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='#3697f5', command=lambda: clear()).place(x=10,y=100)
Button(root, text='/', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('/')).place(x=150,y=100)
Button(root, text='%', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray' , command=lambda: show('%')).place(x=268,y=100)
Button(root, text='*', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('*')).place(x=384,y=100)

Button(root, text='7', width=5, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('7')).place(x=10,y=200)
Button(root, text='8', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('8')).place(x=150,y=200)
Button(root, text='9', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('9')).place(x=268,y=200)
Button(root, text='-', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('-')).place(x=384,y=200)

Button(root, text='4', width=5, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('4')).place(x=10,y=300)
Button(root, text='5', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('5')).place(x=150,y=300)
Button(root, text='6', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('6')).place(x=268,y=300)
Button(root, text='+', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('+')).place(x=384,y=300)

Button(root, text='1', width=5, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('1')).place(x=10,y=400)
Button(root, text='2', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('2')).place(x=150,y=400)
Button(root, text='3', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('3')).place(x=268,y=400)
Button(root, text='=', width=4, height=3, font=('arial',30,'bold',), bd=1,fg='#fff', bg='yellow', command=lambda: calculate()).place(x=384,y=400)


Button(root, text='0', width=10, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('0')).place(x=10,y=500)
Button(root, text='.', width=4, height=1, font=('arial',30,'bold',), bd=1,fg='#fff', bg='gray', command=lambda: show('.')).place(x=268,y=500)

root.mainloop()
