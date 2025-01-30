#FUNCTIONS
def function_name(parameters):
    # code block
    return value


# Example
def add(a, b):
    return a + b
result = add(5, 3)  # result is 8


# Function with variable number of arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Lambda function for quick operations
square = lambda x: x ** 2

# Function with a nested function
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

# Function that raises an exception
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Function with type hints
def concatenate_strings(a: str, b: str) -> str:
    return a + b

# Example usage:
if __name__ == "__main__":
    # Using the multiply function
    print(multiply(2, 3, 4))  # Output: 24

    # Using the lambda function
    print(square(5))  # Output: 25

    # Using the outer function
    my_greeting = outer_function("Hello, World!")
    my_greeting()  # Hello, World!

    # Using the divide function
    try:
        print(divide(10, 0))
    except ValueError as e:
        print(e)  # Output: Cannot divide by zero!

    # Using the concatenate function
    print(concatenate_strings("Hello, ", "World!"))  # Output: Hello, World!




# with parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!


#return values
def square(x):
    return x * x

print(square(4))  # 16


#scope of variables

x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    return x + y

print(my_function())  # 15
# print(y)  # This would raise an error



def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x += 5
        return x
    return inner_function()


# Higher order functions
def apply_function(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply_function(double, 5))  # 10

# Anonymous Functions (Lambda Functions)
square = lambda x: x ** 2

add = lambda x, y: x + y
print(add(2, 3))  # 5


# Decorators
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    return "Display function executed"

print(display())  # Wrapper executed before display



# Closures
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

my_greeting = outer_function("Hello, World!")
my_greeting()  # Hello, World!


# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
    


# Function Annotations
def multiply(x: int, y: int) -> int:
    return x * y
