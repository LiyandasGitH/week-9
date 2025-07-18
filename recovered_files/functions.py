# FUNCTIONS 
# allow you to encapsulate code and reuse it throughout the program
# leads to more readable & more manageable code


'''
def greet(name):
    print(f"Hello, {name}")

greet("Alice")

def add(a, b):
    return a + b

result = add(2, 5)
print(result)
'''

def factor(n):
    if n == 0:
        return 1
    else: 
        return n*factor(n-1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
# function w/ an operational parameter
greet("Bob", "Good Morning")
# "good morning" replaces the default value "hello"

'''
makes the code:
- more readable 
- more organised 
- more reuseable
- easier to understand
'''
