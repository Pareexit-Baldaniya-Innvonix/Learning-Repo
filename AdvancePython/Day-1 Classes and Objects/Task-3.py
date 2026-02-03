# Task 3: Instantiate object from the class
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make: str = make
        self.model: str = model
        self.year: int = year


details = Car("BMW", "M4", 2026)
print(details.make)
print(details.model)
print(details.year)
