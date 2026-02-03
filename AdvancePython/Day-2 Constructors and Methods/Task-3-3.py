# Task 3:
# 3. Static Method:
class Car:
    @staticmethod
    def is_motorized() -> bool:
        return True


print(f"Is a car motorized?: {Car.is_motorized()}")  # calling via the class

my_car = Car()
print(f"Is my_car motorized?: {my_car.is_motorized()}")  # calling via an instance
