my_list = [1,2,3]
print(my_list)
my_list = ['STRING',100,23.2]
print(my_list)
print(len(my_list))
mylist = ['one','two','three']
print(mylist[0])
print(mylist[1])
another_list = ['four','five','six']
print(mylist + another_list)
new_list = mylist + another_list
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('seven')
print(new_list)
new_list.append('eight')
print(new_list)
new_list.pop()
print(new_list)
new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(popped_item)
print(new_list)
new_list.pop(0)
print(new_list)
new_list.pop(-1)
print(new_list)
new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]
print(new_list)
print(num_list)
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)