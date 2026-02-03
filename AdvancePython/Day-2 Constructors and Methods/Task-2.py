# Task 2: parameterized constructure
class Movie:
    def __init__(self, name: str, type: str, cinema: str) -> None:
        self.name: str = name
        self.type: str = type
        self.cinema: str = cinema


movie_data = Movie("Avatar: Fire and Ash", "Action", "Hollywood")
print(f"Movie name: {movie_data.name}")
print(f"Movie type: {movie_data.type}")
print(f"Movie cinema: {movie_data.cinema}")
