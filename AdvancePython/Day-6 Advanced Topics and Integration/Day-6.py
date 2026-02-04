# Exceptions:
class ValueToHighError(Exception):
    pass


def check_value(n):
    if n > 100:
        raise ValueToHighError("Value must be 100 or less!")


try:
    check_value(200)
except ValueToHighError as e:
    print(e)

# How to handle exceptions:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That wasn't a valid number!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution complete.")

# Task 2: Logging
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)

logging.debug("This is a debug message")
logging.info("The program started successfully!")
logging.warning("This is a warning message")
logging.error("An error occured")
logging.critical("The system has crashed")

# Task 3: Event
import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Handler Demo")

        self.label = tk.Label(
            root, text="Press any key or click me!", font=("Arial", 14)
        )
        self.label.pack(pady=50, padx=50)

        self.label.bind("<Button-1>", self.on_click)

        self.root.bind("<Key>", self.on_key)

    def on_click(self, event):
        print(f"Mouse clicked at: x = {event.x}, y = {event.y}")
        self.label.config(text="Mouse Clicked!", fg="blue")

    def on_key(self, event):
        print(f"Key pressed: {event.char}")
        self.label.config(text=f"You pressed: {event.char}", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# Task 4: 'with' statement in file handling
with open("sample.txt", "r") as file:
    data = file.read()
    print(data)
