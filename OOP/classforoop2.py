class Dog():
    # class object attribute
    # same for any instance of a class
    # don't use self keyword because the class object attribute is the same for any instance of a class
    species = 'mammal'
    def __init__(self,breed,name,spots):
        
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed = 'Lab',name = 'Sam',spots = False)
print(my_dog.species)

class Dog():
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    # operations / actions = methods
    def bark(self):
        print('WOOF!')

my_dog = Dog('Lab','Sam')
print(my_dog.bark())

class Dog():
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    # operations / actions = methods
    def bark(self):
        print('WOOF! My name is {}'.format(self.name))

my_dog = Dog('Lab','Sam')
print(my_dog.bark())

class Dog():
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    # operations / actions = methods
    def bark(self,number):
        print('WOOF! My name is {} and the number is {}'.format(self.name,number))

my_dog = Dog('Lab','Sam')
print(my_dog.bark(10))

class Circle():
    # class object attributes
    pi = 3.14
    def __init__(self,radius=  1):
        self.radius = radius
        self.area = radius ** 2 * self.pi
    # method
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)
print(my_circle.area)
print(my_circle.get_circumference())












