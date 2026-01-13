# Day 6: Advanced Topics and Integration

# Task 1: Types of exception
# -> an unexpected event that occurs during program execution
# -> errors that are occured at run time that called exception or logical error

# 1. Built-in Exceptions:
# -> SyntaxError: when syntax error is encountered  --> missing colon after a if statement
# -> ZeroDivisionError: attempt to divide a number by zero  --> 10 / 0
# -> TypeError: operation applied to an object of incorrect type  --> '5' + 2
# -> ValueError: a function gets an argument of the right type but inappropriate Value  --> int("abc")
# -> IndexError: trying to access an index which is out of the range in a list  --> my_list[10]
# -> KeyError: searching for a dictionary key that doesn't exist  --> my_dict['age']
# -> FileNotFoundError: attempting to open a file that does not exist  --> open("ghost_file.txt")
# -> AttributeError: trying to call a method that does not exist for for that object  --> .append() on a string instead of list

# 2. Exception Hierarchy:
# -> All exceptions in python are organized in a 'family tree'
# -> top is BaseException, and most common errors belongs to the Exception class

# BaseException:  --> root of all exceptions
    # KeyboardInterrupt:  --> when user hits ctrl + c
    # SystemExit:  --> program is told to close
    # Exception:  --> for all regular errors

# 3. User-Defined Exceptions:
# -> create own custom exceptions by creating a new class that inherits from the Exception class

# Ex.
# class ValueToHighError(Exception):
#     pass

# def check_value(n):
#     if n > 100:
#         raise ValueToHighError("Value must be 100 or less!")
    
# try:
#     check_value(200)
# except ValueToHighError as e:
#     print(e)

# 4. How to handle exceptions:

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("That wasn't a valid number!")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("Execution complete.")

# Task 2: Logging
# -> built-in way to track events that happens when code runs
# -> we can categorize message by importance and save them to a file for a later review

# -> 5 levels:
# 1. Debug: 10  --> detailed info, when diagnosing problem
# 2. Info: 20  --> confermation that things are working as expected
# 3. Warning: 30  --> an indication that something unexpected happened
# 4. Error: 40  --> due to more serious problem, software has not been able to perform a function
# 5. Critical: 50  --> a serious problem, indicate that program itself may be unable to continue running

import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'app.log',
    filemode = 'w',
    format = '%(name)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debug message")
logging.info("The program started successfully!")
logging.warning("This is a warning message")
logging.error("An error occured")
logging.critical("The system has crashed")

# Task 3: Event
# -> it is an action that happens in the system
# -> computer listen these signals and triggers specific code when they occur

# common events:
# 1. Mouse Events:  --> clicking a button, moving the cursor, or scrolling
# 2. Keyboard Events:  --> pressing a key, releasing a key
# 3. Window Events:  --> resizing a window, closing the app
# 4. System Events:  --> a timer finishing, a file finishing a download

import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Handler Demo")

        self.label = tk.Label(root, text = "Press any key or click me!", font = ("Arial", 14))
        self.label.pack(pady = 50, padx = 50)

        self.label.bind("<Button-1>", self.on_click)

        self.root.bind("<Key>", self.on_key)

    def on_click(self, event):
        print(f"Mouse clicked at: x = {event.x}, y = {event.y}")
        self.label.config(text = "Mouse Clicked!", fg = "blue")

    def on_key(self, event):
        print(f"Key pressed: {event.char}")
        self.label.config(text = f"You pressed: {event.char}", fg = "red")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# Event Patterns:
# 1. <Button-1>: left mouse click  --> event.x, event.y (coordinates)
# 2. <Double-1>: Doulbe click  --> event.num (button number)
# 3. <Return>: Enter key pressed  --> event.widget (the focused element)
# 4. <FocusIn>: Widget gets focus  --> event.type (type of event)
# 5. <Motion>: Mouse moving  --> event.x_root, event.y_root

# Task 4: 'with' statement in file handling
# -> it is a context manager, used to safely and automatically close file even if error occur
# -> replace long try-catch-finally block
# -> imporove readability by reducing unnecessary code
# -> safe file handling

with open("sample.txt", "r") as file:
    data = file.read()
    print(data)

# -> working on two special methods
# 1. __enter__()  --> opens the file
# 2. __exit__()  --> ensures file colses automatically