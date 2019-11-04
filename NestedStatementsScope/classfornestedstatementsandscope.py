x = 25

def printer():
    x = 50
    return x 

print(x)
print(printer())

name = 'This is a global string'
def greet():
    name = 'Sam'
    def hello():
        print('Hello ' + name)
    hello()
print(greet())

name = 'This is a global string'
def greet():
    def hello():
        print('Hello ' + name)
    hello()
print(greet())

# Global
name = 'This is a global string'
def greet():
    # Enclosing
    name = 'Sam'
    def hello():
        # Local
        name = 'Im a Local'
        print('Hello ' + name)
    hello()
print(greet())

x = 50
def func(x):
    print(f'x is {x}')
print(func(x))

x = 50
def func(x):
    print(f'x is {x}')
    # Local reassignment
    x = 200
    print(f'I just locally changed x to {x}')
print(func(x))
print(x)

x = 50
def func():
    global x 
    print(f'x is {x}')
    # Local reassignment
    x = 'New value'
    print(f'I just locally changed global x to {x}')
print(x)
print(func())
print(x)

x = 50
def func(x):
    print(f'x is {x}')
    # Local reassignment
    x = 'New value'
    print(f'I just locally changed global x to {x}')
    return x 
print(x)
print(func(x))
x = func(x)
print(x)





