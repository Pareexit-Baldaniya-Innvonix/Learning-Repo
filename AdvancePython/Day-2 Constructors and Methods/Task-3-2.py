# Task 3:
# 2. Class Method:
class Car:
    total_cars: int = 0

    def __init__(self) -> None:
        Car.total_cars += 1

    @classmethod
    def get_fleet_size(cls) -> str:
        return f"Total cars build: {cls.total_cars}"


car_data = Car()
print(Car.get_fleet_size())  # calling class methods on the Class itself
