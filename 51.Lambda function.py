'''
lambda function = functioon writen in 1 line using lambda keyword
                    accept any number of arguments, but only have one expression
                    (think it's a shortcut)
                    (useful if needed for a short of time, throw away)
                    lambda parameters:expression
'''
#example
'''
def double(x):
    return x * 2

print(double(5))
'''

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name:first_name + last_name 
check_age = lambda age:True if age >= 18 else False
print(double(7))
print(multiply(7,6))
print(add(7,6,4))