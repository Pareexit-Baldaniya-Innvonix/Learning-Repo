# OOPs program

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger_level = 50

    def eat(self):
        self.hunger_level -= 10

    def check_status(self):
        if self.hunger_level <= 20:
            print(f"{self.name} is full and happy!")
        else:
            print(f"{self.name} is still a bit hungry.")


my_pet = Pet("Buddy")
my_pet.eat()
my_pet.eat()
my_pet.eat()
my_pet.check_status()