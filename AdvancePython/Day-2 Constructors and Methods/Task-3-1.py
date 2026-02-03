# Task 3:
# 1. Instance method:
class Car:
    def __init__(self, color: str) -> None:
        self.color: str = color

    def show_color(self) -> None:  # this is instance method
        print(f"The car is {self.color}")


my_car = Car("Blue")
my_car.show_color()
