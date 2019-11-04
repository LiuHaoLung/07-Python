def hello(name = 'Louis'):
    print('The hello() function has been executed!')
    
    def greet():
        return "\t This is the greet func inside hello!"
    
    print(greet())
hello()

def hello(name = 'Louis'):
    print('The hello() function has been executed!')
    
    def greet():
        return "\t This is the greet func inside hello!"
    
    def welcome():
        return "\t This is the welcome func inside hello!"
    
    # 這兩個 print 是在 hello()裡面，要注意縮排的位置
    print(greet())
    print(welcome())

hello()

def hello(name = 'Louis'):
    print('The hello() function has been executed!')
    
    def greet():
        return "\t This is the greet func inside hello!"
    
    def welcome():
        return "\t This is the welcome func inside hello!"
    
    # 這兩個 print 是在 hello()裡面，要注意縮排的位置
    print(greet())
    print(welcome())
    print('This is the end of the hello function!')

hello()

def hello(name = 'Louis'):
    print('The hello() function has been executed!')
    
    def greet():
        return "\t This is the greet func inside hello!"
    
    def welcome():
        return "\t This is the welcome func inside hello!"
    
    print('I am going to return a function!')
    
    if name == 'Louis':
        return greet
    else:
        return welcome

my_new_func = hello('Louis')
print(my_new_func())

def new_decorator(original_func):
    
    def wrap_func():
        
        print('Some extra code, before the original function')
        
        original_func()
        
        print('Some extra code, after the original function!')
    
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!')

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')

func_needs_decorator()