#VARIABLES
# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# String variables can be declared either by using single or double quotes:


# Numeric types
import IPython


age = 25                # Integer
height = 5.9           # Float 
complex_num = 3 + 4j   # Complex number

# String type
name = "John"          # String using double quotes
city = 'New York'      # String using single quotes
message = """This is a
multiline string"""    # Multi-line string

# Boolean type
is_student = True      # Boolean true
is_working = False     # Boolean false

# Sequence types
fruits = ["apple", "banana", "orange"]    # List
coordinates = (10, 20)                    # Tuple
chars = {'a', 'b', 'c'}                  # Set

# Mapping type
person = {                               # Dictionary
    "name": "Alice",
    "age": 30,
    "city": "London"
}

# None type
empty_value = None     # Represents null/none value


### Set Types

my_set = {"apple", "banana"}    # Set
my_frozenset = frozenset({"apple", "banana"})  # Frozen Set



# Printing different variables
print(age)            # Output: 25
print(name)           # Output: John
print(fruits)         # Output: ['apple', 'banana', 'orange']
print(person["city"]) # Output: London
print(my_frozenset) #Output: 

x = "John"
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)