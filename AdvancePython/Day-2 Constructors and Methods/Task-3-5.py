# Task 3:
# 5. Mutators:
class Car:
    def __init__(self, speed: int) -> None:
        self._speed: int = speed

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter  # the mutator
    def speed(self, value: int) -> None:
        if value < 0:
            print("Speed can not be negative")
        else:
            self._speed = value


my_car = Car(60)
my_car.speed = 80  # uses the setter
print(f"Car running at {my_car.speed} km/h.")

my_car.speed = -10  # checks the validation logic
