#LOOPS

# 1. While Loop - repeats code while a condition is True
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# 2. For Loop - iterates over a sequence (list, tuple, string, etc.)
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"Current fruit: {fruit}")

# 3. Range() function with for loop
for i in range(5):  # prints 0 to 4
    print(i)

# 4. Nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# 5. Loop control statements
# Break - exits the loop
for num in range(10):
    if num == 5:
        break
    print(num)

# Continue - skips the current iteration
for num in range(5):
    if num == 2:
        continue
    print(num)

# 6. While loop with else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed!")

# 7. List comprehension - create lists using loops in one line
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]  # Creates: [1, 4, 9, 16, 25]

# 8. Enumerate - get both index and value in loops
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 9. Zip - iterate over multiple sequences simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 10. While loop with multiple conditions
x = 0
y = 5
while x < 5 and y > 0:
    print(f"x: {x}, y: {y}")
    x += 1
    y -= 1

# 11. Loop with else and break
for i in range(5):
    if i == 10:  # This condition will never be True
        break
    print(i)
else:
    print("Loop completed without break!")

# 12. Infinite loop with break condition
counter = 0
while True:
    print(counter)
    counter += 1
    if counter >= 5:
        break

# 13. Dictionary iteration
student_scores = {"Alice": 85, 
                  "Bob": 92, 
                  "Charlie": 78
                  }
for student, score in student_scores.items():
    print(f"{student} scored {score}")

# 14. Nested list comprehension
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
flattened = [num for row in matrix for num in row] 
print(flattened)  # Creates: [1,2,3,4,5,6,7,8,9]