# Task 2: parameterized constructure
from enum import Enum

class Type(Enum):
    ACTION = "Action"
    COMEDY = "Comedy"
    ROMANCE = "Romance"
    HORROR = "Rorror"

class Movie:
    def __init__(self, name: str, type: Enum, cinema: str) -> None:
        self.name: str = name
        self.type: Enum = type
        self.cinema: str = cinema


movie_data = Movie(name="Avatar: Fire and Ash", type=Type.ACTION, cinema="Hollywood")
print(f"Movie name: {movie_data.name}")
print(f"Movie type: {movie_data.type.value}")
print(f"Movie cinema: {movie_data.cinema}")
