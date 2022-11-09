def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz' 
    if input % 3 == 0:
        return 'fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input

print(fizz_buzz(25))


temperature = 35
if temperature > 30:
    print("It's warm")
    print('drink water')
elif temperature > 20:
    print("It's nice")
else:
    print("It's Cold")
print('done')

def fizz_buzz(input):
    if input % 3 and input % 5 == 0:
        print('FizzBuzz')
    elif input%3 == 0:
         print('Fizz')
    elif input % 5 == 0:
        print('Buzz')
    else:
        print(input)
    return 'end'


print(fizz_buzz(15))
