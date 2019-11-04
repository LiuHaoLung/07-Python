def name_function():
    print('Hello')
print(name_function())

def say_hello():
    print('hello')
print(say_hello)

def say_hello(name):
    print('hello ' + name)
print(say_hello('Louis'))

def say_hello(name = 'NAME'):
    print('hello ' + name)
print(say_hello)
result = say_hello('David')
print(say_hello)
result = say_hello('Zach')
print(say_hello)

def say_hello(name = 'NAME'):
    return 'hello ' + name
result = say_hello('Louis')
print(result)

def add(n1,n2):
    return n1 + n2
result = add(20,30)
print(result)

# Find our if the word 'dog' is in a string?
def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False
print(dog_check('My dog ran away'))

def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False
print(dog_check('Dogs are playing in the park'))

def dog_check(mystring):
    return 'dog' in mystring.lower()
print(dog_check('My dog ran away'))

def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay' 
    return pig_word
print(pig_latin('word'))
print(pig_latin('apple'))