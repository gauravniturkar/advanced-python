"""
In Python, a first-class function is a function that is treated like any other variable or object (a "first-class citizen"). This means functions can be handled uniformly throughout the language, with no restrictions on their use compared to other data types like integers or strings. 

Functions can be:
- Assigned to variables
- Passed as arguments to other functions
- Returned from other functions
- Stored in data structures like lists or dictionaries

This flexibility is a core feature of Python's design and enables powerful programming patterns.
"""

def sqare(x):
    """Returns the square of a number."""
    return x * x

# Assigning a function to a variable
square_function = sqare
# square_function = sqare()

print(square_function(5))  # Output: 25
print(sqare)          # Output: 36



def map_function(func, values):
    """Applies a function to each item in a list and returns a new list."""
    results = []
    for value in values:
        results.append(func(value))
    return results

numbers = [1, 2, 3, 4, 5]
squared_numbers = map_function(sqare, numbers) # idhar function ka naam pass kar rahe hain, function call nahi kar rahe


def cube(x):
    """Returns the cube of a number."""
    return x * x * x




def logger(msg):
    def log_message():
        print(f"Log: {msg}")
    return log_message



log_hi = logger("Hello, World!")
log_hi()  # Output: Log: Hello, World!




def html_tag(tag):
    def wrap_text(msg):
        return f"<{tag}>{msg}</{tag}>"
    return wrap_text

print_div = html_tag("div")
print_span = html_tag("span")

print(print_div("This is a division."))  # Output: <div>This is a division.</div>