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
