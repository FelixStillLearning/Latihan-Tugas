#Args = parameter that will pack all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments

def my_function (*args):
    for arg in args:
        print (arg)

my_function(1,2,3,4,5,6,7,8,9,10)

def x (*args):
    print (args[0])
    print (args[7])

x(1,2,3,4,5,6,7,8,9,10)

def x (*args):
    sum = 0
    tambahan = list()
    for i in args:
        sum += i
    print (sum)
x(1,2,3,4,5,6,7,8,9,10)


