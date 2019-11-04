# two.py

import one

print('Top lever in two.py')

one.func()

if __name__ == '__main__':
	print('Two.py is been run directly!')
else:
	print('Two.py has been imported!')