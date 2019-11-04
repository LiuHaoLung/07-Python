def myfunc(a,b):
    #Returns 5% of the sum of a & b
    return sum((a,b)) * 0.05
print(myfunc(40,60))

def myfunc(*args):
    return sum(args) * 0.05
print(myfunc(100,100,200,500,60,70,90))

def myfunc(*args):
    print(args)
print(myfunc(100,100,200,500,60,70,90))

def myfunc(*spam):
    print(spam)
print(myfunc(100,200,300,500))

def myfunc(*args):
    for item in args:
        print(item)
print(myfunc(100,200,300,500))        

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I didn't find any fruit here")
print(myfunc(fruit = 'apple'))       
print(myfunc(fruit = 'apple',veggie = 'lettuce'))

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
print(myfunc(10,20,30,fruit = 'orange',food = 'eggs',aniaml = 'cat'))