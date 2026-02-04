# OOPs Program


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        super().__init__(self)
        return "Meow!"


animals = [Dog("Rex"), Cat("Whiskers")]

for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
