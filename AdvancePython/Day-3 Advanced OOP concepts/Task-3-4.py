# Task 3:
# 4. Method Overriding:
class A:
    def func1(self) -> None:
        print("Feature 1 of class A")

    def func2(self) -> None:
        print("Feature 2 of class A")


class B(A):
    def func1(self) -> None:
        print("Modified feature 1 of class A by class B")

    def func3(self) -> None:
        print("Feature 3 of class B")


obj = B()
obj.func1()
