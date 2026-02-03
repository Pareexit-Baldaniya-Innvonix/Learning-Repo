# Task 1: simple constructure
from enum import Enum


# using enumiration for toy size
class Size(Enum):  # IntEnum for integer values
    SMALL = "small"  # also use interger values for Enum
    MEDIUM = "medium"
    LARGE = "large"


class Toy:
    def __init__(self, name: str, size: Size) -> None:
        self.name: str = name
        self.size: Size = size


my_toy = Toy(name="Bear", size=Size.MEDIUM)
my_lion = Toy(name="Lion", size=Size.LARGE)
print(f"Name: {my_toy.name} | Size: {my_toy.size.value}")
print(f"Name: {my_lion.name} | Size: {my_lion.size.value}")
