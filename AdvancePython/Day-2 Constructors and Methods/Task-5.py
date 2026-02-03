# Task 5:
class Car:
    age = 20

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make: str = make
        self.model: str = model
        self.year: int = year

    @property
    def age(self) -> int:
        current_year: int = 2026
        return current_year - self.year


my_car = Car("BMW", "M4", 2024)
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
print(f"Age: {my_car.age} years")
