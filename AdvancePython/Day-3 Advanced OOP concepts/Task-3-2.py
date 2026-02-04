# Task 3:
# 2. Constructors:
def __init__(self) -> None:
    # body of the constructor
    pass


class Parent:
    def __init__(self, item: list[int]) -> str:
        self.item: list[int] = item
        print(f"Parent class: {self.item}")


class SubClass(Parent):
    def __init__(self, item: list[int]) -> None:
        super().__init__(item)
        print(f"Output of SubClass")


data = [1, 2, 3, 4, 5]
instance = SubClass(data)
