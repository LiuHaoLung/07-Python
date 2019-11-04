print('This is a string{}'.format('INSERTED'))
print('The {} {} {}'.format('fox','brown','quick'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {0} {0} {0}'.format('fox', 'brown','quick'))
print('The {q} {b} {f}'.format(f = 'fox', b = 'brown' , q = 'quick'))
print('The {f} {f} {f}'.format(f = 'fox', b = 'brown' , q = 'quick'))
result = 100/777
print('The result was {}'.format(result))
print('The result was {r}'.format(r = result))
print('The result was {r:1.3f}'.format(r = result))
print('The result was {r:10.3f}'.format(r = result))
print('The rusult was {r:10.5f}'.format(r = result))
print('The rusult was {r:1.2f}'.format(r = result))
name = "Jose"
print('Hello, his name is {}'.format(name))
print(f'Hello, his name is {name}')
name = 'Sam'
age = 3
print(f'{name} is {age} years old.')
print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))
x,y = 'some','note'
print("I'm going to inject %s text here , amd %s text here."%(x,y))