# Object-Oriented Programming (Classes, Objects, Inheritance)

# - **Classes and Objects**: Understand the difference between a class (blueprint) and an object (instance).
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

bj = Car("Toyota", "Corolla") #object
print(bj.make)  # Toyota

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"


#Attributes
class Car:
    def __init__(self, make, model, year):
        self.make = make      # Attribute for the make of the car
        self.model = model    # Attribute for the model of the car
        self.year = year      # Attribute for the year of the car


#Methods
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "Engine started!"
    

#Complete Example
class Car:
    def __init__(self, make, model, year):
        self.make = make      # Attribute for the make of the car
        self.model = model    # Attribute for the model of the car
        self.year = year      # Attribute for the year of the car

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"  # Method to display car information

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())  # Output: 2020 Toyota Corolla

#Encapsulation
#Public Attributes
class Car:
    def __init__(self, make, model):
        self.make = make      # Public attribute
        self.model = model    # Public attribute

class Profession:
    def __init__(self, name, position):
        self.name = name      # Public attribute
        self.position = position   # Public attribute        


#Private Attributes
class Car:
    def __init__(self, make, model):
        self.__make = make      # Private attribute
        self.__model = model    # Private attribute

    def display_info(self):
        return f"{self.__make} {self.__model}"  # Method to display car information
    
bh = Car("Toyota", "Corolla")
print(bh.display_info())  # Output: Toyota Corolla
    

#Accessing Private Attributes
class Car:
    def __init__(self, make, model):
        self.__make = make    # Private attribute
        self.__model = model   # Private attribute

    def get_make(self):      # Getter method for make
        return self.__make

    def get_model(self):     # Getter method for model
        return self.__model

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")
print(my_car.get_make())  # Output: Toyota
print(my_car.get_model()) # Output: Corolla

#Using Properties
#### Example with Getters and Setters
class Car:
    def __init__(self, make, model):
        self.__make = make      # Private attribute
        self.__model = model    # Private attribute

    @property
    def make(self):           # Getter for make
        return self.__make

    @make.setter
    def make(self, value):    # Setter for make
        if isinstance(value, str):
            self.__make = value
        else:
            raise ValueError("Make must be a string.")

    @property
    def model(self):          # Getter for model
        return self.__model

    @model.setter
    def model(self, value):   # Setter for model
        if isinstance(value, str):
            self.__model = value
        else:
            raise ValueError("Model must be a string.")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")
print(my_car.make)  # Output: Toyota
print(my_car.model) # Output: Corolla

# Using the setter to change the make
my_car.make = "Honda"
print(my_car.make)  # Output: Honda

# Attempting to set an invalid value
try:
    my_car.make = 123  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: Make must be a string.