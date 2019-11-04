import sys

print(sys.argv)
print(sys.argv[0])

for argument in sys.argv:
    if sys.argv.index(argument) == 0:
        print("This is a file name: " + argument)
    else:
        print('This is an argument: ' + argument)

for index,argument in enumerate(sys.argv[1:]):
    print('Argument ' + str(index) + ': ' + argument)