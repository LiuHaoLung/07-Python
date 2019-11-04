class Dog():
    def __init__(self,breed):
        self.breed = breed
my_dog = Dog(breed = 'Lab')

print(my_dog.breed)


class Dog():    
    def __init__(self,mybreed):
        self.breed = mybreed

my_dog = Dog(mybreed = 'Huskie')
print(my_dog.breed)

class Dog():
    def __init__(self,breed,name,spots):
        # every attribute you pass in this going to any data type
        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots

my_dog = Dog(breed = 'Lab',name = 'Sammy',spots = False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)