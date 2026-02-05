# Task 1: Pickling
import pickle

# constants
DATA_FILE = "AdvancePython/Day-8 Error Handling/data.pkl"
USER_DATA = {"name": "world", "age": 25}


# pickling
def save_data(obj: dict, filename: str) -> None:
    with open(filename, "wb") as file:
        pickle.dump(obj, file)
    print(f"Data successfully pickled to {filename} file.")


# depickling
def load_data(filename: str) -> dict:
    with open(filename, "rb") as file:
        return pickle.load(file)


if __name__ == "__main__":
    save_data(USER_DATA, DATA_FILE)

    loaded_data = load_data(DATA_FILE)
    print(f"Deserialized object: {loaded_data}")
