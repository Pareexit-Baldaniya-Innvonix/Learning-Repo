# Task 4:
class Employee:
    class Address:
        def __init__(self, country: str) -> None:
            self.country: str = country

        def display(self) -> None:
            print(f"Address: {self.country}")

    def __init__(self, name: str, country: str = "India") -> None:
        self.name = name
        self.addr = self.Address(country)

    def show(self) -> None:
        print(f"Name: {self.name}")
        self.addr.display()


e1 = Employee("Virat")
e1.show()
