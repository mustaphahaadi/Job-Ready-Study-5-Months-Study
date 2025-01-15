#DATA TYPES AND OPERATORS

#DATA TYPES
#int
#float
#str
#bool

#OPERATORS
#arithmetic operators
#assignment operators
#comparison operators
#logical operators
#identity operators
#membership operators
#bitwise operators

#ARITHMETIC OPERATORS
print(5+6)    # Output: 11
print(5-6)    # Output: -1
print(5*6)    # Output: 30
print(5/6)    # Output: 0.8333333333333334
print(5//6)   # Output: 0
print(5%6)    # Output: 5
print(5**6)   # Output: 15625

#ASSIGNMENT OPERATORS
x=5
x+=7
print(x)    # Output: 12

#COMPARISON OPERATORS
i=5
print(i==5)   # Output: True
print(i!=5)   # Output: False
print(i>5)    # Output: False
print(i<5)    # Output: False
print(i>=5)   # Output: True
print(i<=5)   # Output: True

#LOGICAL OPERATORS
a=True
b=False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
print(not b)    # Output: True

#IDENTITY OPERATORS
a=True
b=False
print(a is b)      # Output: False
print(a is not b)  # Output: True

#MEMBERSHIP OPERATORS
list=[1,2,3,4,5,6,7,8,9,10]
print(5 in list)       # Output: True
print(15 in list)      # Output: False
print(5 not in list)   # Output: False
print(15 not in list)  # Output: True

#BITWISE OPERATORS
#0-00
#1-01
#2-10
#3-11
print(0 & 1)   # Output: 0
print(0 | 1)   # Output: 1
print(0 | 3)   # Output: 3
print(0 ^ 3)   # Output: 3
print(0 >> 2)  # Output: 0
print(0 << 2)  # Output: 0


# Integers - whole numbers, positive or negative
x = 5
y = -17
big_num = 1_000_000  # Can use underscores for readability

# Converting to int
float_to_int = int(3.14)    # 3
str_to_int = int("100")     # 100
binary = 0b1010             # 10 in decimal
octal = 0o12               # 10 in decimal
hexadecimal = 0x0A         # 10 in decimal

print(type(x))  # <class 'int'>



# Floating point numbers
x = 3.14
y = -0.001
scientific = 2.5e-3  # 0.0025

# Converting to float
int_to_float = float(5)      # 5.0
str_to_float = float("3.14") # 3.14

# Float precision
print(0.1 + 0.2)  # 0.30000000000000004 (floating-point precision issue)

# Comparison with different types
print(5 == 5.0)      # True (value equality)
print(5 is 5.0)      # False (identity comparison)

# String comparison
print("apple" < "banana")  # True (lexicographical comparison)
print("5" == 5)           # False (different types)

# Multiple comparisons
x = 5
print(1 < x < 10)    # True (chained comparison)

# Strings - text enclosed in quotes
single = 'Hello'
double = "World"
multi_line = '''This is a
multi-line string'''

# String operations
name = "Python"
print(name[0])      # 'P' (indexing)
print(name[1:4])    # 'yth' (slicing)
print(name * 2)     # 'PythonPython' (repetition)
print(name + "3.x") # 'Python3.x' (concatenation)

# String methods
text = " Hello, World! "
print(text.strip())      # Remove whitespace
print(text.lower())      # Convert to lowercase
print(text.upper())      # Convert to uppercase
print(text.split(","))   # Split into list

# Boolean values - True or False
x = True
y = False

# Boolean conversion
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("text"))  # True
print(bool([]))      # False
print(bool([1, 2]))  # True

a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.3333...
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000

# Real-world example
price = 100
tax_rate = 0.2
total = price + (price * tax_rate)
print(f"Total price with tax: ${total}")  # $120.0


x = 5
x += 3   # x = x + 3
print(x)  # 8

x -= 2   # x = x - 2
print(x)  # 6

x *= 2   # x = x * 2
print(x)  # 12

x /= 3   # x = x / 3
print(x)  # 4.0

x //= 2  # x = x // 2
print(x)  # 2.0

x %= 2   # x = x % 2
print(x)  # 0.0

y = 2
y **= 3  # y = y ** 3
print(y)  # 8


# Comparison with different types
print(5 == 5.0)      # True (value equality)
print(5 is 5.0)      # False (identity comparison)

# String comparison
print("apple" < "banana")  # True (lexicographical comparison)
print("5" == 5)           # False (different types)

# Multiple comparisons
x = 5
print(1 < x < 10)    # True (chained comparison)

# Logical operators with non-boolean values
print([] and "hello")     # [] (short-circuit evaluation)
print([] or "hello")      # "hello"
print("" or "default")    # "default"

# Common use cases
user_input = ""
name = user_input or "Anonymous"  # Default value if input is empty
print(name)  # "Anonymous"

# Short-circuit evaluation
x = 5
y = 0
print(y != 0 and x/y)  # False (avoids division by zero)

# Membership operators with different collections
string = "Hello World"
list_nums = [1, 2, 3, 4, 5]
tuple_data = (1, "hello", 3.14)
set_items = {1, 2, 3}
dict_data = {"name": "John", "age": 30}

# in operator
print("Hello" in string)        # True
print(2 in list_nums)          # True
print("hello" in tuple_data)   # True
print(4 in set_items)          # False
print("name" in dict_data)     # True (checks keys)

# Identity operators with objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list2)     # False (different objects)
print(list1 is list3)     # True (same object)
print(list1 == list2)     # True (same values)

# Explicit type conversion
num_int = 123
num_float = 3.14
num_str = "456"
str_float = "3.14"

print(float(num_int))    # 123.0
print(int(num_float))    # 3
print(int(num_str))      # 456
print(float(str_float))  # 3.14
print(str(num_int))      # "123"

# Error handling in conversion
try:
    int("hello")  # ValueError
except ValueError as e:
    print(f"Conversion error: {e}")