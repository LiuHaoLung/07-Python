def add(n1,n2):
    print(n1+n2)

add(10,20)

try:
    # Want to attempt this code
    # May have an error
    result = 10 + 10
except:
    print('Hey it looks like you are not adding correcttly')

print(result)

try:
    # Want to attempt this code
    # May have an error
    result = 10 + '10'
except:
    print('Hey it looks like you are not adding correcttly')


try:
    # Want to attempt this code
    # May have an error
    result = 10 + '10'
except:
    print('Hey it looks like you are not adding correcttly')
else:
    print('Add went well!')
    print(result)

try:
    # Want to attempt this code
    # May have an error
    result = 10 + 10
except:
    print('Hey it looks like you are not adding correcttly')
else:
    print('Add went well!')
    print(result)

try:
    f = open('testfile','w')
    f.write('Write a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS Error')
finally:
    print('I always run')

try:
    f = open('testfile','r')
    f.write('Write a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS Error')
finally:
    print('I always run')

try:
    f = open('testfile','r')
    f.write('Write a test line')
except TypeError:
    print('There was a type error!')
except:
    print('All other exceptions!')
finally:
    print('I always run')

def ask_for_int():
    try:
        result = int(input('Please provide number: '))
    except:
        print('Whoops! That is not a number')
    finally:
        print('End of try/except/finally')

ask_for_int()

def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops! That is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('End of try/except/finally')
            print('I will always run at the end!')

ask_for_int()

def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops! That is not a number')
            continue
        else:
            print('Yes thank you')
            break

ask_for_int()