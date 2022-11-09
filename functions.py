'''
def multiply(*numbers):
    total = 2
    for number in numbers:
        total = total *number
    return total


print(multiply(2, 3, 4, 5))

def save_user(**users):
    for user in users:
        print(user)


save_user(id=1, name='John', age=22)

def save_users(**users):
    print(users['name'])


save_users(id=1, name='John', age=22)
'''

message = 'a'

def greet(user):
    message = 'b'


greet('Tim')

print(bs(-5)