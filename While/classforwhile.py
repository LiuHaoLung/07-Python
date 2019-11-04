x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1

x = 0
while x < 5:
    x = x + 1
    print(f'The current value of x is {x}')

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print('X is not less than 5')

x = 50
while x < 5:
    print(f'The current value of x is {x}')
else:
    print('X is not less than 5')

x = [1,2,3]
for item in x:
    #comment
    pass
print('end of my script')

mystring = 'Sammy'
for letter in mystring:
    print(letter)

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

num = 10
while num > 0:
    num = num - 1 
    if num == 5:
        continue
    print(f'Now num is {num}')
else:
    print('The loop is over')

num = 0
while num < 10:
    num = num + 1
    if num % 2 == 0:
        continue
    print(f'This is Odd num:{num}')

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)

even_num = []
odd_num = []
num = 0
while num < 100:
    num = num + 1
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)
print(even_num)
print(odd_num)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1