# Task 5:
class Calculator:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def sub(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def mul(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def div(a: int, b: int) -> float:
        return a / b


print(f"Addition: {Calculator.add(10, 5)}")
print(f"Subtraction: {Calculator.sub(10, 5)}")
print(f"Multiplication: {Calculator.mul(10, 5)}")
print(f"Division: {Calculator.div(10, 8)}")
