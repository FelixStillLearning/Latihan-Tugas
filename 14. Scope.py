#Scope = a region of a program where a variable is recognized
#        A variable is only available from inside the region it is created in
#        Global Scope = a variable created in the main body of the program
#        Local Scope = a variable created inside a function or method
#        Built-in Scope = a variable created in the pre-defined python library
#        Nonlocal Scope = a variable created inside a nested function
#        Enclosing Scope = a variable created inside a function's local scope
#        a global and local locally version can be created in the same scope

Name = "Felix" #Global Scope (available inside and outside the function)

def display_name ():
    Name = "Angga" #local scope (available only inside the function)
    print (Name)

display_name()
print(Name)
#LEGB rules = Local, Enclosing, Global, Built-in

#enclosing scope
def outer_function():
    x = 10  # Outer function variable
    
    def inner_function():
        y = 5  # Inner function variable
        result = x + y  # Accessing outer function variable
        print(result)
    
    inner_function()

outer_function()

