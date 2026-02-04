# OOPs Program


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h.")


class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed)
        self.battery = battery

    def silence_mode(self):
        print(
            f"The {self.brand} is now driving silently because it has a {self.battery}% battery!"
        )


my_tesla = ElectricCar("Tesla", 120, 100)
my_tesla.drive()
my_tesla.silence_mode()
