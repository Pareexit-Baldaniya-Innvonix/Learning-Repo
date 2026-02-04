# Task 1: Pickling
import pickle

data = {"name": "world", "age": 25}  # python object

pickle.dump(
    data, open("data.pkl", "wb")
)  # serialize the object. 'wb' - write in binary mode
load = pickle.load(
    open("data.pkl", "rb")
)  # read the file and deserialize into python object
print(load)


# Task 3:
class FileEmptyError(Exception):
    pass


import os


def read_and_print_file(filename):
    try:
        if os.path.exists(filename) and os.path.getsize(filename) == 0:
            raise FileEmptyError(f"The file '{filename}' contains no data.")

        with open(filename, "r") as file:
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
