'''
high order function = a function that either accepts or returns a function as
                     an argument and retuen an argument.
'''

def loud(text):
    return text.upper()
def quite(text):
    return text.lower()

def hello(func):
    text = func("hello")
    print(text)

hello(loud)
hello(quite)

print("------------------")

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))