# Task 4:
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make: str = make
        self.model: str = model
        self.year: int = year


car_details = Car("BMW", "M4", 2026)
print(f"Make: {car_details.make}")
print(f"Model: {car_details.model}")
print(f"Year: {car_details.year}")
