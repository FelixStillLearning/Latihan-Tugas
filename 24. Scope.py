#Scope = where a variable is recognized
#        local if it is inside a function
#        global if it is outside a function
#        built-in if it is pre-defined in Python
#        nonlocal if it is inside a nested function
#        enclosing if it is inside a nested function

# LEGB = Local, Enclosing, Global, Built-in

Nama = "Felix" #Global Scope

def display_name ():
    Nama = "Angga" #Local Scope 
    print (Nama)

display_name()
print (Nama)

#enclosing scope
def outer_function():
    x = 10  # Outer function variable
    
    def inner_function():
        nonlocal x
        y = 5  # Inner function variable
        result = x + y  # Accessing outer function variable
        print(result)
    
    inner_function()
    
outer_function()