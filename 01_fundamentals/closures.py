"""
A closure in Python is a function object that has access to variables in its enclosing (outer) function's scope, even after the outer function has finished executing. 
In essence, a closure "remembers" the environment in which it was created, allowing it to retain and use state information without relying on global variables or classes. 
"""


def outer_function():
    msg = 'hi'
    def inner_function():
        print(msg)
    return inner_function()

outer_function()