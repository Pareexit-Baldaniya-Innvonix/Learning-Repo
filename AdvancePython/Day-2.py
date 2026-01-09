# Day 2: Constructors and Methods

# Task 1: simple constructure
# class Toy:
#     def __init__(self):
#         self.name = "Bear"
#         self.size = "small"

# toy = Toy()
# print(toy.name)
# print(toy.size)

# Task 2: parameterized constructure
class Movie:
    def __init__(self, name, type, cinema):
        self.name = name
        self.type = type
        self.cinema = cinema

movie = Movie("Avatar: Fire and Ash", "Action", "Hollywood")
print(movie.name)
print(movie.type)
print(movie.cinema)

# Task 3:
# 1. Instance method:
# -> used to access or change data belonging to a specific object
# -> always take self as a first argument
# -> use for describing action to specific item

class Car:
    def __int__(self):
        self.color = "Blue"

    def show_color(self):  # this is instance method
        print(f"the car is {self.color}")

# 2. Class Method:
# -> belongs to class itself
# -> used to see and change the things which affect every object created from that class
# -> using @classmethod decorator
# -> take cls as first argument

class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def get_fleet_size(cls):
        return f"total cars build: {cls.total_cars}"
    
# 3. Static Method:
# -> related to class
# -> they don't need to know anything about class and object
# -> used as a general tool
# -> use @staticmethod

class Car:
    @staticmethod
    def isMotorized():
        return True
    
# 4. Accessors:
# -> used to access a piece of data without changing it
# -> @property decorator used for it
# -> take self as a first argument

class Car:
    def __init__(self, brand):
        self._brand = brand
    
    @property
    def brand_name(self):
        return self._brand.upper()
    
# 5. Mutators:
# -> used to change a piece of data
# -> useful because allow to add "rules" before change
# -> take self, value as a first arguments

class Car:
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if value < 0:
            print("Speed can not be negative")
        else:
            self._speed = value

# Task 4:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

Car_details = Car("BMW", "M4", 2026)
print(Car_details.make)
print(Car_details.model)
print(Car_details.year)

# Task 5:
class Car:
    age = 20
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @property
    def age(self):
        current_year = 2026
        return current_year - self.year

Car_details = Car("BMW", "M4", 2024)
print(Car_details.make)
print(Car_details.model)
print(Car_details.year)
print(Car_details.age)