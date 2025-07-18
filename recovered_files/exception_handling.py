# EXCEPTIONS
'''
deals w/ runtime errors & exceptions
an exception is an event that occurs during the execution of a prgramme
disruptiong the normal flow of the execution
try: code that may raise an exception
except: code that will execute if an exception occurs
finally: executes the code regardless of the exception
else: will execute if no exceptions are raised in try block
raise(manually): throw an exception if a particular condition is met 
'''

try:
    print(x)
#x is undefined
except NameError:
    print("Variable x is not defined")
#except:
#    print("Something went wrong")
#finally:
#    print("The 'try except' is finished")
else:
    print("Everything went wrong")

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

