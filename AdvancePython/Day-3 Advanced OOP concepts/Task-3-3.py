# Task 3:
# 3. Method overloading:
def add_values(datatype: str, *args: any) -> None:
    if datatype == "int":
        answer = 0
    elif datatype == "str":
        answer = ""
    else:
        print(f"Different datatype!")

    for x in args:
        answer += x
    print(answer)


add_values("int", 5, 6)
add_values("str", "Hello ", "World")
