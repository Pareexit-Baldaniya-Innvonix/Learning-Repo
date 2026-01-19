# Day 7: Decorators in Python

# Task 1: Decorators
# -> decorators are function that takes function and return it with some additional functionalities
# -> it is a wrapper funtion that modifies the behaviour
# -> use '@' symbol for assigning a decorator to the function

def changeCase(func):
    def myInner():
        return func().upper()
    return myInner()

@changeCase
def myFunc():
    return "Hello World!"

print(myFunc)

# Task 2:
# -> it is like a blueprint for other classes
# -> define common interface for all subclasses
# -> provide shared functionality

# @abstractmethod:
# -> it is a decorator
# -> used inside a ABC(Abstract Base Class) to define a required behavior without providing a actual code for it
# -> in logic only contains pass
# -> it catches design error before code is running

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
dog = Dog()
print(dog.sound())

# Task 3:

def greetings(func):
    def wrapper():  # nested function
        print("Hello!")
        func()
        print("How are you?")
    return wrapper

@greetings
def world():
    print(", World")

world()
# --> o/p = Hello!, World  --> before function runs, decorator works
#           How are you?  --> after function run, decorator not works

# Task 4:
# -> built-in decorators are like a 'tags' that python provides

# 1. @property:
# -> used to make a methods look and act like a variable
# -> use with parentheses '()'

# 2. @staticmethod:
# -> methods in a class need to know about the object they belong to
# -> uses self as a first argument

# 3. @classmethod:
# -> it looks at the entire class
# -> uses cls as first argument, not self
# -> creating a new object from a different data type

# 4. @functools.lru_cache:
# -> build-in decorator from the functools library
# -> speeding up complex problems

# Ex.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * (self.radius ** 2)
    
c = Circle(5)
print(c.area)

# Task 5:
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # start time
        result = func(*args, **kwargs) # actual function
        end_time = time.perf_counter() # end time
        print(f"Time taken: {end_time - start_time:.4f} seconds.") # calculate and print duration
        return result
    return wrapper

@timer # decorator
def waste_time():
    time.sleep(1)
    print("Function finished!")
waste_time()