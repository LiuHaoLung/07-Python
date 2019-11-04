mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

for new_string in mylist:
    print('hello')

for even_num in mylist:
    #check for even num
    if even_num % 2 == 0:
        print(even_num)

for num in mylist:
    if num % 2 == 0:
        print(f'Even num: {num}')
    else:
        print(f'Odd num: {num}')

for num in mylist:
    if num % 2 == 0:
        print(f'Even num: {num}')
    else:
        print('Odd num: {}'.format(num))

list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(list_sum)

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)

mystring = 'Hello World'
for letter in mystring:
    print(letter)

for letter in 'Hello World':
    print(letter)

for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num)

for _ in 'Hello World':
    print('Cook!')

for _ in 'Hello World':
    print(_)

tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]
len(mylist)
for item in mylist:
    print(item)

for (a,b) in mylist:
    print(a)
    print(b)

for (a,b) in mylist:
    print(a)

for a,b in mylist:
    print(a)
    print(b)

mylist = [(1,2,3),(4,5,6),(7,8,9)]
for item in mylist:
    print(item)

for a,b,c in mylist:
    print(a,b,c)

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

for item in d.items():
    print(item)

for key,value in d:
    print(value)

for key,value in d.items():
    print(value)

for value in d.values():
    print(value)

mylist = [{'a':1,'b':2},{'c':3,'d':4},{'e':5,'f':6}]
for d in mylist:
    for k,v in d.items():
        print(f'k is {k} and v is {v}')

primelist = []

for num in range(0,100):
    if num % 2 == 0:
        print(num)
    elif num % 3 == 0:
        print(num)
    elif num % 5 == 0:
        print(num)
    elif num % 7 == 0:
        print(num)
    else:
        primelist.append(num)

print(primelist)