#CONTROL FLOW (IF/ELSE, LOOPS)


#if/else Statements syntax
#if condition:
    # code to execute if condition is True
#else:
    # code to execute if condition is False

# Multiple Conditions (elif)
from multiprocessing.spawn import is_forking


score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print("Your grade is:", grade)


# 1. if/else Statements
age = 18
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")


# Logical Operators with conditionals
# and: both conditions must be True
if age >= 18 and has_license:
    print("Can drive")

# or: at least one condition must be True
if is_holiday or is_weekend:
    print("Day off!")

# not: inverts the condition
if not is_forking:
    print("Free time!")

# 2. while loops syntax
#while condition:
    # code to repeat while condition is True
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# 3. for loops
# Iterating through a range
for i in range(3):
    print(f"Number: {i}")

# iterating through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# 4. Break and Continue
# Break example
for i in range(10):
    if i == 5:
        break  # exits the loop
    print(i)

# Continue example
for i in range(5):
    if i == 2:
        continue  # skips the rest of the loop for this iteration
    print(f"Current number: {i}")

# 5. Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")



# Counter loop
count = 0
while count < 5:
    print(count)
    count += 1

# User input validation
password = ""
while password != "secret":
    password = input("Enter password: ")



# Range with one argument (stop)
for i in range(5):  # 0 to 4
    print(i)

# Range with start and stop
for i in range(2, 5):  # 2 to 4
    print(i)

# Range with start, stop, and step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Iterating over sequences
for char in "Python":  # String
    print(char)

for item in [1, 2, 3]:  # List
    print(item)

for key, value in {"a": 1, "b": 2}.items():  # Dictionary
    print(f"Key: {key}, Value: {value}")

# List Comprehension
# Traditional for loop
squares = []
for x in range(5):
    squares.append(x**2)

# Same thing as list comprehension
squares = [x**2 for x in range(5)]

# Else executes when loop completes normally (no break)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")