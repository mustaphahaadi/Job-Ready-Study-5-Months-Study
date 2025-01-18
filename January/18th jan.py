#FUNCTIONS

# Basic function definition
def greet():
    print("Hello, World!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Function with default parameter
def greet_with_title(name, title="Mr."):
    print(f"Hello {title} {name}!")

# Function that returns a value
def add_numbers(a, b):
    return a + b

# Function with multiple returns
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Function with arbitrary arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

# Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
if __name__ == "__main__":
    # Basic function call
    greet()  # Output: Hello, World!
    # Calling function with argument
    greet_person("Alice")  # Output: Hello, Alice!
    # Using default                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    greet_with_title("Bob")  # Output: Hello Mr. Bob!
    greet_with_title("Alice", "Dr.")  # Output: Hello Dr. Alice!
    
    # Function with return value
    result = add_numbers(5, 3)
    print(result)  # Output: 8
    
    # Multiple returns
    numbers = [1, 2, 3, 4, 5]
    minimum, maximum = get_min_max(numbers)
    print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 1, Max: 5
    
    # Using *args
    total = sum_all(1, 2, 3, 4, 5)
    print(f"Sum: {total}")  # Output: Sum: 15
    
    # Using **kwargs
    print_info(name="Alice", age=30, city="New York")
    # Output:
    # name: Alice
    # age: 30
    # city: New York
