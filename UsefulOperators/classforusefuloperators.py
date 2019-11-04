mylist = [1,2,3]
for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

for num in range(0,10,2):
    print(num)

range(0,11,2)
list(range(0,11,2))

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item)

word = 'abcde'
for index,letter in enumerate(word):
    print(f'The word index is {index} and the letter is {letter}')

word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
zip(mylist1,mylist2)

for item in zip(mylist1,mylist2):
    print(item)

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

list(zip(mylist1,mylist2))

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for a,b,c in zip(mylist1,mylist2,mylist3):
    print(f'First is {a},seconde is {b} and third is {c}')

print('x' in [1,2,3])
print('x' in ['x','y','z'])

mylist = [1,2,3]
print(2 in mylist)

print('a' in 'a world')

print('mykey' in {'mykey':345})

d = {'mykey':345}
print(345 in d.values())
print(345 in d.keys())

mylist = [10,20,30,100]
print(min(mylist))
print(max(mylist))

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))
print(randint(0,100))

