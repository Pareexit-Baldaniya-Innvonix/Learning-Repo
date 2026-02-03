# Task 2: class with basic attribute
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make: str = make
        self.model: str = model
        self.year: int = year
