# Task 3:
# 1. Inheritance:
class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def info(self) -> None:
        print(f"Animal name: {self.name}")


class Dog(Animal):
    def sound(self) -> None:
        print(f"{self.name} barks")


dog = Dog("Buddy")
dog.info()
dog.sound()
