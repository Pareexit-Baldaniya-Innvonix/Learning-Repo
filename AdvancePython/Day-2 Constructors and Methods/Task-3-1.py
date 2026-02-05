# Task 3:
# 1. Instance method:
from enum import Enum


class Color(Enum):
    BLUE = "blue"
    RED = "red"
    BLACK = "black"
    WHITE = "white"


class Car:
    def __init__(self, color: Enum) -> None:
        self.color: Enum = color

    def show_color(self) -> None:  # this is instance method
        print(f"The car color is {self.color}")


my_car = Car(f"{Color.BLACK.value}")
my_car.show_color()
