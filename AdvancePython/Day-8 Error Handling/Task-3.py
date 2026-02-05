# Task 3:
import os


class FileEmptyError(Exception):
    pass


def read_and_print_file(filename: str) -> None:
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

if __name__ == "__main__":
    read_and_print_file("ghost.txt") # missing file

    open("empty.txt", "w").close()
    read_and_print_file("empty.txt") # empty file
