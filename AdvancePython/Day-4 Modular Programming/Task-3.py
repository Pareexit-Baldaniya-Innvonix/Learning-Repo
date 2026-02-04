# Task 3: Decorators
def changecase(func: str) -> str:
    def myinner() -> str:
        return func().upper()

    return myinner


@changecase
def myfunction() -> str:
    return "Hello World!"


print(myfunction())
