# Task 1: Decorators
def changeCase(func):
    def myInner():
        return func().upper()

    return myInner()


@changeCase
def myFunc():
    return "Hello World!"


print(myFunc)

# Task 2:
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


# Task 4:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * (self.radius**2)


c = Circle(5)
print(c.area)

# Task 5:
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # start time
        result = func(*args, **kwargs)  # actual function
        end_time = time.perf_counter()  # end time
        print(
            f"Time taken: {end_time - start_time:.4f} seconds."
        )  # calculate and print duration
        return result

    return wrapper


@timer  # decorator
def waste_time():
    time.sleep(1)
    print("Function finished!")


waste_time()
