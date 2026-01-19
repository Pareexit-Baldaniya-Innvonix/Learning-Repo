# Day 8: Error Handling

# Task 1: Pickling
# -> this is the process of converting a object into byte stream
# -> using that it can be saved to a file or transmitted over a network

# Ex.
import pickle

data = {'name': 'world', 'age': 25} # python object

pickle.dump(data, open('data.pkl', 'wb')) # serialize the object. 'wb' - write in binary mode
load = pickle.load(open('data.pkl', 'rb')) # read the file and deserialize into python object
print(load)

# Task 2: Exceptions and handling

# Exceptions:

# 1. ZeroDivisionError -> divide by zero (5 / 0)
# 2. ValueError -> correct data type but inappropriate value int("hello")
# 5. IndexError -> trying to access an list index which is not exist 
# 6. TypeError -> operation applied to wrong datatype
# 7. KeyError -> trying to access a dictionary key that hasn't been defined
# 8. FileNotFoundError -> trying to access the file which is not exist

# Exception Handling:

# try:
    # code
# except SomeException:
    # code
# except SomeException:
    # code
# else:
    # code
# finally:
    # code

# Task 3:
class FileEmptyError(Exception):
    pass

import os

def read_and_print_file(filename):
    try:
        if os.path.exists(filename) and os.path.getsize(filename) == 0:
            raise FileEmptyError(f"The file '{filename}' contains no data.")
    
        with open(filename, 'r') as file:
            content = file.read()
            print("--File Content--")
            print(content)
            print("----------------")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except FileEmptyError as e:
        print(f"Custom Error: {e}")

    except Exception as e:
        print(f"An unexpected error occured: {e}")

read_and_print_file("ghost.txt")

open("empty.txt", "w").close()
read_and_print_file("empty.txt")