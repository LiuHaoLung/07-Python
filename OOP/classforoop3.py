class Animal():
    def __init__(self):
        print('Animal created')
    # method
    def who_am_i(self):
        print('I am an animal')
    # method
    def eat(self):
        print('I am eating')

myanimal = Animal()
print(myanimal)
print(myanimal.eat())
print(myanimal.who_am_i())

class Dog(Animal):
    def __init__(self):
        # 繼承了父類別
        Animal.__init__(self)
        print('Dog created')

mydog = Dog()
print(mydog)
print(mydog.eat())

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    def who_am_i(self):
        print('I am a dog!')

mydog = Dog()
print(mydog)
print(mydog.eat())
print(mydog.who_am_i())

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    def bark(self):
        print('WOOF!')
    def eat(self):
        print('I am a dog and eating')

mydog = Dog()
print(mydog)
print(mydog.eat())
print(mydog.who_am_i())
print(mydog.bark())


class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says meow!'

niko = Dog('Niko')
felix = Cat('Felix')
print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

print(pet_speak(niko))
print(pet_speak(felix))

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

class Dog(Animal):
    def speak(self):
        return self.name + ' says woof!'

class Cat(Animal):
    def speak(self):
        return self.name + ' says meow!'

fido = Dog('Fido')
isis = Cat('Isis')
print(fido.speak())
print(isis.speak())