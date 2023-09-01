# Decorator is a function that takes a function as input and output a modified version

def announce(f):
    def wrapper():
        print("About to run a function!")
        f()
        print("Completed")
    return wrapper

@announce
def hello():
    print("Hello World!")

'''
Potential Uses:
    - A decorator that allows access to features only if a user is logged in.
'''